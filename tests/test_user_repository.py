from lib.user_repository import *
from lib.user import *
from werkzeug.security import check_password_hash

def test_initialise_user_repository(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    assert isinstance(repository, UserRepository)

def test_login_correct_login(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_1', 'password_1')
    assert user == {'id': 1, 'username': 'username_1'}

def test_login_incorrect_username(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_5', 'password_1')
    assert user == False

def test_login_incorrect_password(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_1', 'password_5')
    assert user == False

def test_login_incorrect_username_and_password(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user = repository.login('username_5', 'password_10')
    assert user == False
    
def test_find_user_with_id_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user(1)
    assert user == User(1, 
                        'username_1', 
                        'name_1', 
                        'scrypt:32768:8:1$n952oFWoS88c2UCd$b030f2524c51d45b866f128a92335d05d3be6ec27c0c153d4db9e58514ffbab4f4bea39d93694cfd5ae4eb2d51f6a10b866ae87057a7cd246f4eadf37576308d', 
                        'email_1@gmail.com', 
                        '07777111111')
    
def test_find_user_with_id_2(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user(2)
    assert user == User(2, 
                        'username_2', 
                        'name_2', 
                        'scrypt:32768:8:1$lj6tuvqbfBTNIcMx$e8b2b2fe230d39e1f2afc1b07efcf578ee3a5fca9d0fe86d54f0ed8a7fb8118e1330edccac8d317069ed944a4d55f8ca56a14bcf13734d43aae9eff172080dc1', 
                        'email_2@gmail.com', 
                        '07777222222')
    
def test_add_user(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user_to_add = User(None, 'username_4', 'name_4', 'password_4', 'email_4@gmail.com', '07777444444')
    repository.create_user(user_to_add)
    user = repository.find_user(4)
    assert user.id == 4
    assert user.username == 'username_4'
    assert user.name == 'name_4'
    assert check_password_hash(user.password, 'password_4') == True
    assert user.email == 'email_4@gmail.com'
    assert user.phone_number == '07777444444'
    
def test_update_user(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    user_to_update = User(1, 'username_6', 'name_6', 'password_6', 'email_6@gmail.com', '07777666666')
    repository.update_user(user_to_update)
    user = repository.find_user(1)
    assert user.id == 1
    assert user.username == 'username_6'
    assert user.name == 'name_6'
    assert check_password_hash(user.password, 'password_6') == True
    assert user.email == 'email_6@gmail.com'
    assert user.phone_number == '07777666666'
    
def test_delete_user(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    repository.delete_user(2)
    user = repository.find_user(2)
    assert user == None