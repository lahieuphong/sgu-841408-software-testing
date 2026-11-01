import pytest
from regis import register_user, RegistrationError

def test_empty_username():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("", "test@example.com", "Password123")
    assert str(exc_info.value) == "Username cannot be empty"

def test_invalid_email_format():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("username", "invalid-email", "Password123")
    assert str(exc_info.value) == "Invalid email format"

def test_password_too_weak():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("username", "test@example.com", "123")
    assert str(exc_info.value) == "Password too weak"

def test_password_missing_uppercase():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("username", "test@example.com", "password123")
    assert str(exc_info.value) == "Password must contain at least one uppercase letter"

def test_successful_registration():
    result = register_user("username", "test@example.com", "Password123")
    assert result == "Registration successful"

def test_missing_domain_in_email():
    with pytest.raises(RegistrationError) as exc_info:
        register_user("username", "user@com", "Password123")
    assert str(exc_info.value) == "Invalid email format"

def test_password_with_special_characters():
    result = register_user("username", "test@example.com", "Password@123")
    assert result == "Registration successful"


if __name__ == "__main__":
    test_empty_username()
    test_invalid_email_format()
    test_password_too_weak()
    test_password_missing_uppercase()
    test_successful_registration()
    test_missing_domain_in_email()
    test_password_with_special_characters()
