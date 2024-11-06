from validation_methods import *

def test_check_string_not_empty():
    assert check_string_not_empty("Hello") is True
    
    assert check_string_not_empty("") is None
    assert check_string_not_empty(None) is None

def test_check_there_are_no_spaces():
    assert check_there_are_no_spaces("NoSpaces") is True
    
    assert check_there_are_no_spaces("Has Spaces") is False
    assert check_there_are_no_spaces("") is True

def test_check_name_is_valid():
    assert check_name_is_valid("Name") is True
    
    assert check_name_is_valid("") == "Name must be 1-30 characters and not empty."
    assert check_name_is_valid(" ") == "Name must be 1-30 characters and not empty."
    assert check_name_is_valid("Name123") == "Name must not contain numbers."
    
def test_check_username_is_valid():
    assert check_username_is_valid("User1") is True
    
    assert check_username_is_valid("") == "Username must be 2-17 characters long with no spaces."
    assert check_username_is_valid(" ") == "Username must be 2-17 characters long with no spaces."
    assert check_username_is_valid("U") == "Username must be 2-17 characters long with no spaces."
    assert check_username_is_valid("User 1") == "Username must be 2-17 characters long with no spaces."

def test_check_password_is_valid():
    assert check_password_is_valid("Password1") is True
    
    assert check_password_is_valid("Pass1") == "Password must be 8-255 characters with atleast one letter and number."
    assert check_password_is_valid("12345678") == "Password must be 8-255 characters with atleast one letter and number."
    assert check_password_is_valid("Password") == "Password must be 8-255 characters with atleast one letter and number."
    assert check_password_is_valid(" ") == "Password must be 8-255 characters with atleast one letter and number."

def test_check_phone_number_is_valid():
    assert check_phone_number_is_valid("07777777777") is True
    
    assert check_phone_number_is_valid("077777777") == "Phone number must be 10-11 digits with no spaces"
    assert check_phone_number_is_valid("077777777777") == "Phone number must be 10-11 digits with no spaces"
    assert check_phone_number_is_valid("0777 7777 777") == "Phone number must be 10-11 digits with no spaces"
    assert check_phone_number_is_valid("aaaaaaaaaaa") == "Phone number must be 10-11 digits with no spaces"

def test_check_email_is_valid():
    assert check_email_is_valid("user@example.com") is True
    
    assert check_email_is_valid("userexample.com") == "Email must be 5-255 characters and include a domain"
    assert check_email_is_valid("u@.c") == "Email must be 5-255 characters and include a domain"
    assert check_email_is_valid("user@com") == "Email must be 5-255 characters and include a domain"
    assert check_email_is_valid("") == "Email must be 5-255 characters and include a domain"

def test_check_signup_valid():
    errors = check_signup_valid("ValidName", "test@example.com", "1234567890", "ValidUser", "Password1")
    assert all(error is True for error in errors)

    errors = check_signup_valid("", "test@example.com", "1234567890", "ValidUser", "Password1")
    assert "Name must be 1-30 characters and not empty." in errors

    errors = check_signup_valid("ValidName", "testexample.com", "1234567890", "ValidUser", "Password1")
    assert "Email must be 5-255 characters and include a domain" in errors

    errors = check_signup_valid("ValidName", "test@example.com", "123456789", "ValidUser", "Password1")
    assert "Phone number must be 10-11 digits with no spaces" in errors

    errors = check_signup_valid("ValidName", "test@example.com", "1234567890", "User Name", "Password1")
    assert "Username must be 2-17 characters long with no spaces." in errors

    errors = check_signup_valid("ValidName", "test@example.com", "1234567890", "ValidUser", "short1")
    assert "Password must be 8-255 characters with atleast one letter and number." in errors