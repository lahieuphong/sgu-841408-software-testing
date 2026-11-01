#!/usr/bin/env python3
"""Restore the encrypted original-history archive using a recovery key."""
import argparse
import base64
import getpass
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import struct

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

FORMAT = "sgu-private-archive-v1"
ALGORITHM = "AES-256-GCM"
MAGIC = b"SGUENC1\n"
PART_LIMIT = 40 * 1024 * 1024
PAYLOAD_LIMIT = 256 * 1024 * 1024


def decode_key(value):
    value = value.strip()
    try:
        raw = base64.b64decode(value + "=" * (-len(value) % 4), altchars=b"-_", validate=True)
    except (ValueError, UnicodeError) as error:
        raise ValueError("The recovery key is not valid URL-safe Base64.") from error
    if len(raw) != 32:
        raise ValueError("The recovery key must encode exactly 32 bytes.")
    return raw


def associated_data(manifest):
    header = {name: manifest[name] for name in ("format", "algorithm", "archive_id")}
    if header["format"] != FORMAT or header["algorithm"] != ALGORITHM:
        raise ValueError("Unsupported archive format or encryption algorithm.")
    if not isinstance(header["archive_id"], str) or not re.fullmatch(r"[0-9a-f]{32}", header["archive_id"]):
        raise ValueError("Invalid archive identifier.")
    return json.dumps(header, sort_keys=True, separators=(",", ":")).encode("ascii")


def read_ciphertext(manifest_path):
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Invalid archive manifest.")
    aad = associated_data(manifest)
    parts = manifest.get("parts")
    total = manifest.get("ciphertext_bytes")
    if not isinstance(parts, list) or not 1 <= len(parts) <= 16:
        raise ValueError("Invalid encrypted part list.")
    if type(total) is not int or not 16 <= total <= PAYLOAD_LIMIT:
        raise ValueError("Invalid or unsupported payload size.")
    chunks = []
    collected = 0
    for index, part in enumerate(parts):
        expected_name = f"payload.part-{index:03d}"
        if not isinstance(part, dict) or part.get("name") != expected_name:
            raise ValueError("Part names or order are invalid.")
        size = part.get("bytes")
        digest = part.get("sha256")
        if type(size) is not int or not 0 < size <= PART_LIMIT:
            raise ValueError(f"Invalid size for {expected_name}.")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"Invalid checksum for {expected_name}.")
        source = manifest_path.parent / expected_name
        info = source.stat()
        if source.is_symlink() or not stat.S_ISREG(info.st_mode) or info.st_size != size:
            raise ValueError(f"Unexpected file type or size: {expected_name}.")
        data = source.read_bytes()
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f"Checksum mismatch: {expected_name}.")
        chunks.append(data)
        collected += size
        if collected > total:
            raise ValueError("Encrypted parts exceed the declared size.")
    ciphertext = b"".join(chunks)
    if collected != total or hashlib.sha256(ciphertext).hexdigest() != manifest.get("ciphertext_sha256"):
        raise ValueError("The combined encrypted payload failed its integrity check.")
    try:
        nonce = base64.b64decode(manifest["nonce"], validate=True)
    except (KeyError, ValueError, TypeError) as error:
        raise ValueError("Invalid encryption nonce.") from error
    if len(nonce) != 12:
        raise ValueError("Invalid encryption nonce length.")
    return ciphertext, nonce, aad


def decrypt_archive(manifest_path, key):
    ciphertext, nonce, aad = read_ciphertext(manifest_path)
    # AESGCM verifies the authentication tag before returning any plaintext.
    plaintext = AESGCM(key).decrypt(nonce, ciphertext, aad)
    prefix = len(MAGIC) + 4
    if len(plaintext) < prefix or not plaintext.startswith(MAGIC):
        raise ValueError("Decrypted archive header is invalid.")
    length = struct.unpack(">I", plaintext[len(MAGIC):prefix])[0]
    if not 1 <= length <= 65536 or prefix + length > len(plaintext):
        raise ValueError("Decrypted metadata size is invalid.")
    metadata = json.loads(plaintext[prefix:prefix + length].decode("utf-8"))
    if not isinstance(metadata, dict):
        raise ValueError("Decrypted archive metadata is invalid.")
    archive = plaintext[prefix + length:]
    filename = metadata.get("filename")
    if not isinstance(filename, str) or filename in (".", "..") or filename != Path(filename).name or not re.fullmatch(r"[A-Za-z0-9._-]+", filename):
        raise ValueError("Decrypted archive filename is invalid.")
    if type(metadata.get("bytes")) is not int or len(archive) != metadata["bytes"]:
        raise ValueError("Decrypted archive length does not match its metadata.")
    if hashlib.sha256(archive).hexdigest() != metadata.get("sha256"):
        raise ValueError("Decrypted archive checksum does not match its metadata.")
    return archive, metadata


def restore_archive(manifest_path, key, output=None):
    archive, metadata = decrypt_archive(manifest_path, key)
    destination = Path(output) if output is not None else Path.cwd() / "restored-private" / metadata["filename"]
    destination.parent.mkdir(parents=True, exist_ok=True)
    # O_EXCL also refuses an existing symlink, including a dangling symlink.
    fd = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(archive)
    except BaseException:
        destination.unlink(missing_ok=True)
        raise
    return destination, metadata


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("manifest.json"))
    parser.add_argument("--output", type=Path, help="New output file; existing files are never overwritten.")
    parser.add_argument("--key-file", type=Path, help="File containing the Base64 recovery key; prompts if omitted.")
    args = parser.parse_args()
    try:
        value = args.key_file.read_text(encoding="ascii").strip() if args.key_file else getpass.getpass("Recovery key (hidden): ")
        destination, metadata = restore_archive(args.manifest, decode_key(value), args.output)
    except InvalidTag:
        parser.exit(1, "Authentication failed: the key is incorrect or the encrypted archive was changed.\n")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Restore failed: {error}\n")
    print(f"Restored and verified {metadata['bytes']:,} bytes to {destination}")
    print("The restored archive contains private originals. Keep it outside version control.")


if __name__ == "__main__":
    main()
