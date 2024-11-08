from lib.user_repository import UserRepository
from lib.database_connection import get_flask_database_connection
from flask import Flask
app = Flask(__name__)

def check_string_not_empty(entry):
    if entry != "" and entry != " " and entry != None:
        return True
    
def check_there_are_no_spaces(entry):
    if " " in entry:
        return False
    else:
        return True
    
def check_name_is_valid(entry):
    if len(entry) > 0 and len(entry) <= 30 and check_string_not_empty(entry):
        if any(char.isdigit() for char in entry):
            return "Name must not contain numbers."
        return True
    else:
        return "Name must be 1-30 characters and not empty."
    
def check_username_is_valid(entry, original_username=None):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    username_unique = True
    for username_email_pair in repository.get_usernames_emails():
        print(f'checking if{original_username} = {entry}')
        if username_email_pair['username'] == entry and original_username!=entry:
            username_unique = False 
    if len(entry) > 2 and len(entry)<= 17 and check_string_not_empty(entry) and check_there_are_no_spaces(entry) and username_unique:
        return True
    else:
        return "Username must be unique and 2-17 characters long with no spaces."

def check_password_is_valid(entry):
    has_letter = any(char.isalpha() for char in entry)
    has_number = any(char.isdigit() for char in entry)
    if has_letter and has_number and len(entry) > 7 and len(entry)<= 255 and check_string_not_empty(entry) and check_there_are_no_spaces(entry):
        return True
    else:
        return "Password must be 8-255 characters with at least one letter and number."

def check_phone_number_is_valid(entry):
    has_number = any(char.isdigit() for char in entry)
    is_number = True
    for char in entry:
        if not char.isdigit():
            is_number = False
    if len(entry) > 9 and len(entry)<= 11 and is_number and check_string_not_empty(entry):
        return True
    else:
        return "Phone number must be 10-11 digits with no spaces."

def check_email_is_valid(entry, original_email=None):
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    email_unique = True
    for username_email_pair in repository.get_usernames_emails():
        if username_email_pair['email'] == entry and original_email !=entry:
            email_unique = False 
    if "." in entry and "@" in entry and len(entry) > 5 and len(entry)<= 255 and check_string_not_empty(entry) and check_there_are_no_spaces(entry) and email_unique:
        return True
    else:
        return "Email must be unique with 5-255 characters and include a domain."

def check_signup_valid(name, email, phone_number, username, password):
    errors = []
    errors.append(check_name_is_valid(name))
    errors.append(check_email_is_valid(email))
    errors.append(check_phone_number_is_valid(phone_number))
    errors.append(check_username_is_valid(username))
    errors.append(check_password_is_valid(password))
    return errors

def check_profile_update_valid(username, email, phone_number, name, original_username, original_email):
    errors = []
    errors.append(check_username_is_valid(username,original_username))
    errors.append(check_email_is_valid(email,original_email))
    errors.append(check_phone_number_is_valid(phone_number))
    errors.append(check_name_is_valid(name))
    return errors

# Space related validation:
def check_space_name_is_valid(entry):
    if len(entry) >=3 and len(entry) <=30 and check_string_not_empty:
        return True
    else:
        return 'Space name must be 3-30 characters.'
    
def check_address_is_valid(entry):
    if len(entry) >=8 and len(entry) <=255 and check_string_not_empty:
        return True
    else:
        return 'Address must be 8-255 characters.'
    
def check_description_is_valid(entry):
    if len(entry) >=8 and len(entry) <=255 and check_string_not_empty:
        return True
    else:
        return 'Description must be 8-255 characters.'

def check_price_is_valid(entry):
    try:
        float(entry)
        return True
    except ValueError:
        return 'Price must be a float'

def check_space_creation_valid(name,address,description,price):
    errors =[]
    errors.append(check_space_name_is_valid(name))
    errors.append(check_address_is_valid(address))
    errors.append(check_description_is_valid(description))
    errors.append(check_price_is_valid(price))
    return errors