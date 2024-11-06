def check_string_not_empty(entry):
    if entry != "" and entry != None:
        return True
    
def check_there_are_no_spaces(entry):
    if " " in entry:
        return False
    else:
        return True
    
def check_name_is_valid(entry):
    if len(entry) > 0 and len(entry) <= 30 and entry != " " and check_string_not_empty(entry):
        if any(char.isdigit() for char in entry):
            return "Name must not contain numbers."
        return True
    else:
        return "Name must be 1-30 characters and not empty."
    
def check_username_is_valid(entry):
    if len(entry) > 2 and len(entry)<= 17 and check_string_not_empty(entry) and check_there_are_no_spaces(entry):
        return True
    else:
        return "Username must be 2-17 characters long with no spaces."

def check_password_is_valid(entry):
    has_letter = any(char.isalpha() for char in entry)
    has_number = any(char.isdigit() for char in entry)
    if has_letter and has_number and len(entry) > 7 and len(entry)<= 255 and check_string_not_empty(entry) and check_there_are_no_spaces(entry):
        return True
    else:
        return "Password must be 8-255 characters with atleast one letter and number."

def check_phone_number_is_valid(entry):
    has_number = any(char.isdigit() for char in entry)
    is_number = True
    for char in entry:
        if not char.isdigit():
            is_number = False
    if len(entry) > 9 and len(entry)<= 11 and is_number and check_string_not_empty(entry):
        return True
    else:
        return "Phone number must be 10-11 digits with no spaces"

def check_email_is_valid(entry):
    if "." in entry and "@" in entry and len(entry) > 5 and len(entry)<= 255 and check_string_not_empty(entry) and check_there_are_no_spaces(entry):
        return True
    else:
        return "Email must be 5-255 characters and include a domain"

def check_signup_valid(name, email, phone_number, username, password):
    errors = []
    errors.append(check_name_is_valid(name))
    errors.append(check_email_is_valid(email))
    errors.append(check_phone_number_is_valid(phone_number))
    errors.append(check_username_is_valid(username))
    errors.append(check_password_is_valid(password))
    return errors