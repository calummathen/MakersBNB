from lib.user_repository import *
from lib.user import *
from werkzeug.security import check_password_hash
from datetime import *

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
    assert user.email == 'email_6@gmail.com'
    assert user.phone_number == '07777666666'
    
def test_delete_user(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = UserRepository(db_connection)
    repository.delete_user(2)
    user = repository.find_user(2)
    assert user == None

def test_search_for_everything_as_owner_1(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_owner(1)
    print(user)
    assert user == User(1, 'username_1', 'name_1', None, 'email_1@gmail.com', '07777111111', [
        Space(1, 'Stratfest', 'Wembley', 'Company event space', 1000.50, '[2024-09-14, 2024-09-15, 2024-09-16]', 1, [

            Booking(1, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-07', '%Y-%m-%d').date(), 1, 1, 1, 6003, True),
            Booking(2, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 2, 1, 1, 5002.5, True),
            Booking(3, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 4002, False),
            Booking(4, datetime.strptime('2024-12-22', '%Y-%m-%d').date(), datetime.strptime('2024-12-23', '%Y-%m-%d').date(), 2, 1, 1, 1000.5, True),
            Booking(5, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 1, 1, 1, 6003,False),
            Booking(7,  datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-03', '%Y-%m-%d').date(), 4, 1, 1, 2001, True)
    ]),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1, [
            Booking(6, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 2, 2, 1, 1200, True),
            Booking(8, datetime.strptime('2024-12-08', '%Y-%m-%d').date(), datetime.strptime('2024-12-15', '%Y-%m-%d').date(), 5, 2, 1, 1400, False),
            Booking(17, datetime.strptime('2024-12-28', '%Y-%m-%d').date(), datetime.strptime('2025-01-02', '%Y-%m-%d').date(), 7, 2, 1, 1000,True)
        ]),
        Space(5, 'Conference Center', '99 Main St', 'Large event venue', 1500.75, '[2024-09-20, 2024-09-21, 2024-09-22]', 1, [
            Booking(12, datetime.strptime('2024-12-15', '%Y-%m-%d').date(), datetime.strptime('2024-12-18', '%Y-%m-%d').date(), 8, 5, 1, 4502.25, True)
        ])
    ])

def test_search_for_everything_as_guest_1(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_guest(1)
    assert user == User(1, 'username_1', 'name_1', None, 'email_1@gmail.com', '07777111111', [
        Space(1, 'Stratfest', 'Wembley', 'Company event space', 1000.50, '[2024-09-14, 2024-09-15, 2024-09-16]', 1, [
            Booking(1, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-07', '%Y-%m-%d').date(), 1, 1, 1, 6003, True),
            Booking(3, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 4002, False),
            Booking(5, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 1, 1, 1, 6003, False)
    ])
    ])

def test_search_for_everything_as_owner_2(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_owner(2)
    print(user)
    assert user == User(2, 
                        'username_2', 
                        'name_2', 
                        None,
                        'email_2@gmail.com', 
                        '07777222222', [
        Space(3, 'Big Hotel','4 Street','Dangerous area', 150.99,'[]', 2, [
            Booking(9, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 6, 3, 2, 603.96, True),
            Booking(18, datetime.strptime('2025-01-05', '%Y-%m-%d').date(), datetime.strptime('2025-01-10', '%Y-%m-%d').date(), 4, 3, 2, 754.95, False)

        ])
    ])

def test_search_for_everything_as_guest_2(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_guest(2)
    assert user == User(2, 'username_2', 'name_2', None, 'email_2@gmail.com', '07777222222', [
        Space(1, 'Stratfest', 'Wembley', 'Company event space', 1000.50, '[2024-09-14, 2024-09-15, 2024-09-16]', 1, [

            Booking(2, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 2, 1, 1, 5002.5, True),
            Booking(4, datetime.strptime('2024-12-22', '%Y-%m-%d').date(), datetime.strptime('2024-12-23', '%Y-%m-%d').date(), 2, 1, 1, 1000.5, True),

    ]),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1, [
            Booking(6, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 2, 2, 1, 1200.0, True)
        ])
    ])

def test_search_for_everything_as_owner_3(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_owner(3)
    assert user == User(3, 'username_3','name_3', None, 'email_3@gmail.com', '07777333333', [
        Space(4, 'Small House','5 street','Peterborough',00.00,'[]', 3, [
            Booking(10, datetime.strptime('2024-12-20', '%Y-%m-%d').date(), datetime.strptime('2024-12-25', '%Y-%m-%d').date(), 3, 4, 3, 0, True),
            Booking(11, datetime.strptime('2024-12-10', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 7, 4, 3, 0, False)
        ])
    ])

def test_search_for_everything_as_guest_3(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_guest(3)
    assert user == User(3, 'username_3','name_3', None, 'email_3@gmail.com', '07777333333', [
        Space(4, 'Small House','5 street','Peterborough',00.00,'[]', 3, [
            Booking(10, datetime.strptime('2024-12-20', '%Y-%m-%d').date(), datetime.strptime('2024-12-25', '%Y-%m-%d').date(), 3, 4, 3, 0, True),
        ]),
        Space(9, 'City Apartment', '100 Urban St', 'Cozy city apartment', 120.00, '[2024-12-15, 2024-12-20]', 8, [
            Booking(16, datetime.strptime('2024-12-20', '%Y-%m-%d').date(), datetime.strptime('2024-12-27', '%Y-%m-%d').date(), 3, 9, 8, 840, True)
        ])
    ])

def test_search_for_everything_as_owner_4(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_owner(4)
    assert user == User(4, 'username_4', 'name_4', None, 'email_4@gmail.com', '07777444444', [])

def test_search_for_everything_as_guest_4(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_guest(4)
    assert user == User(4, 'username_4', 'name_4', None, 'email_4@gmail.com', '07777444444', [
        Space(1, 'Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1, [
            Booking(7, datetime.strptime('2024-12-01', '%Y-%m-%d').date(),datetime.strptime('2024-12-03', '%Y-%m-%d').date(), 4, 1, 1, 2001, True)
        ]),
        Space(3, 'Big Hotel','4 Street','Dangerous area',150.99,'[]', 2, [
            Booking(18,  datetime.strptime('2025-01-05', '%Y-%m-%d').date(), datetime.strptime('2025-01-10', '%Y-%m-%d').date(), 4, 3, 2, 754.95, False)
        ]),
        Space(6, 'Art Gallery', '1 Art St', 'Modern and spacious', 500.00, '[2024-10-01, 2024-10-02]', 5, [
            Booking(13, datetime.strptime('2024-11-05', '%Y-%m-%d').date(), datetime.strptime('2024-11-10', '%Y-%m-%d').date(), 4, 6, 5, 2500, True)
        ])
    ])

def test_search_for_everything_as_owner_6(db_connection):
    db_connection.seed("seeds/extensive_database.sql")
    repository = UserRepository(db_connection)
    user = repository.find_all_information_as_owner(6)
    assert user == User(6, 'username_6', 'name_6', None, 'email_6@gmail.com', '07777666666', [
        Space(7, 'Beach House', '10 Beach Ave', 'Seaside retreat', 300.00, '[2024-11-10, 2024-11-15]', 6, [
            Booking(14, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-05', '%Y-%m-%d').date(), 5, 7, 6, 1200, True)
        ]),
        Space(12, 'Farmhouse', '9 Country Rd', 'Countryside farmhouse', 80.00, '[2024-12-25, 2024-12-30]', 6, [])
    ])




