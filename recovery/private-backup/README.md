# Encrypted original history and private files

This folder preserves the complete original 124,878,186-byte backup without removing or changing any of its contents. It includes seven original nested Git histories and the five original files saved before publication, including the original account data. Installed environments, browser profiles and caches are not part of this archive.

The archive is encrypted with AES-256-GCM. Its recovery key is delivered separately in the owner's chat and is not stored in this repository. **Keep that key: the archive cannot be restored without it.**

## Restore after cloning

From the repository root, using Python 3.12 or newer:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r recovery/private-backup/requirements.txt
.venv/bin/python recovery/private-backup/restore.py
```

Paste the recovery key at the hidden prompt. The default output is `restored-private/sgu-841408-private-backup-2026-11-01.tar.gz`, which is excluded from Git. Existing files are never overwritten. To choose a different location, pass `--output /path/to/private-backup.tar.gz`.

The script checks each encrypted part, authenticates and decrypts the combined payload, then verifies the original archive's size and SHA-256 checksum before writing the output. No private archive contents are extracted or executed by the script.

To inspect and extract the restored archive locally:

```bash
tar -tzf restored-private/sgu-841408-private-backup-2026-11-01.tar.gz
mkdir -p restored-private/extracted
tar -xzf restored-private/sgu-841408-private-backup-2026-11-01.tar.gz -C restored-private/extracted
```

`nested-git/` contains the original Git metadata; `original-files/` contains the original saved files. `SHA256.json` records the checksums of all 15,371 archived private files. `RESTORE-INFO.txt` explains the original backup.

## Archive layout

`manifest.json` lists the ordered encrypted parts and their ciphertext checksums. Each part is at most 40 MiB. Sensitive filenames, the original archive checksum and its contents are inside the authenticated encryption. The format and recovery code are inspectable; the recovery key and decrypted data remain private.

[Course overview](../../README.md)
