from lib.user import *

def test_initialise_user():
    id = 1
    username = "username"
    name = "name"
    email = "example@gmail.com"
    phone_number = "07777552233"
    password = "password"
    user = User(id, username, name, password, email, phone_number)
    assert user.id == id
    assert user.username == username
    assert user.name == name
    assert user.password == password
    assert user.email == email
    assert user.phone_number == phone_number
    assert user.spaces == []


def test_compare_two_users_with_same_details():
    id = 1
    username = "username"
    name = "name"
    email = "example@gmail.com"
    phone_number = "07777552233"
    password = "password"
    user = User(id, username, name, password, email, phone_number)
    comparison_user = User(id, username, name, password, email, phone_number)
    assert user == comparison_user


def test_string_representation_of_user():
    id = 1
    username = "username"
    name = "name"
    email = "example@gmail.com"
    phone_number = "07777552233"
    password = "password"
    user = User(id, username, name, password, email, phone_number)
    user_string = str(user)
    assert user_string == "User(1, username, name, password, example@gmail.com, 07777552233, [])"

