from lib.user_repository import *
from lib.user import *

def test_initialise_user_repository(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    assert isinstance(repository, UserRepository)

def test_login_correct_login(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_1', 'password_1')
    assert user == {'id': 1, 'username': 'username_1'}

def test_login_incorrect_username(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_5', 'password_1')
    assert user == 'Incorrect username or password'

def test_login_incorrect_password(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_1', 'password_5')
    assert user == 'Incorrect username or password'

def test_login_incorrect_username_and_password(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_5', 'password_10')
    assert user == 'Incorrect username or password'
    
def test_find_user_with_id_1(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user(1)
    assert user == User(1, 'username_1', 'name_1', 'password_1', 'email_1@gmail.com', '07777111111')
    
def test_find_user_with_id_2(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user(2)
    assert user == User(2, 'username_2', 'name_2', 'password_2', 'email_2@gmail.com', '07777222222')
    
def test_add_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user_to_add = User(None, 'username_3', 'name_3', 'password_3', 'email_3@gmail.com', '07777333333')
    repository.create_user(user_to_add)
    assert repository.find_user(3) == User(3, 'username_3', 'name_3', 'password_3', 'email_3@gmail.com', '07777333333')
    
def test_update_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    user_to_update = User(1, 'username_4', 'name_4', 'password_4', 'email_4@gmail.com', '07777444444')
    repository.update_user(user_to_update)
    assert repository.find_user(1) == User(1, 'username_4', 'name_4', 'password_4', 'email_4@gmail.com', '07777444444')
    
def test_delete_user(db_connection):
    db_connection.seed("seeds/user.sql")
    repository = UserRepository(db_connection)
    repository.delete_user(2)
    user = repository.find_user(2)
    assert user == None