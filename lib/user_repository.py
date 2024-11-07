from lib.user import *
from werkzeug.security import check_password_hash, generate_password_hash
from lib.space import Space
from lib.booking import Booking
from helper_functions import calculate_total_price

class UserRepository:
    def __init__(self, connection):
        self._connection = connection


    def login(self, username, password):
        attempted_user = self._connection.execute('SELECT * FROM users WHERE username = %s', [username])
        if len(attempted_user) == 0:
            return False
        user = attempted_user[0]
        correct_password = check_password_hash(user['password'], password)
        if correct_password == False:
            return False
        return {'id': user['id'], 'username': user['username']}
        
    def find_user(self, id):
        try:
            result = self._connection.execute("SELECT * FROM users WHERE id = %s", [id])[0]
        except IndexError:
            return None
        id = result["id"]
        username = result["username"]
        name = result["name"]
        password = result["password"]
        email = result["email"]
        phone_number = result["phone_number"]
        user = User(id, username, name, password, email, phone_number)
        return user

    def create_user(self, user_to_add):
        hashed_password = generate_password_hash(user_to_add.password)
        self._connection.execute("INSERT INTO users (username, name, password, email, phone_number) VALUES(%s, %s, %s, %s, %s)", 
        [user_to_add.username, user_to_add.name, hashed_password, user_to_add.email, user_to_add.phone_number]
        )
        
    def update_user(self, user_to_update):
        # hashed_password = generate_password_hash(user_to_update.password)
        self._connection.execute("UPDATE users SET username=%s, name=%s, email=%s, phone_number=%s WHERE id = %s", 
        [user_to_update.username, user_to_update.name, user_to_update.email, user_to_update.phone_number, user_to_update.id])
        
    def delete_user(self, id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [id])

    def get_usernames_emails(self):
        result = self._connection.execute("SELECT username,email FROM users")
        return result
    
    def find_all_information_as_owner(self, user_id):
        user_information = self._connection.execute('SELECT\
                                                    users.id AS owner_id,\
                                                    users.username,\
                                                    users.name AS name,\
                                                    users.email,\
                                                    users.phone_number,\
                                                    spaces.id AS space_id,\
                                                    spaces.name AS space_name,\
                                                    spaces.address,\
                                                    spaces.description,\
                                                    spaces.price,\
                                                    spaces.dates_booked,\
                                                    spaces.owner_id AS space_owner_id,\
                                                    bookings.id AS booking_id,\
                                                    bookings.check_in,\
                                                    bookings.check_out,\
                                                    bookings.user_id AS user_id,\
                                                    bookings.space_id AS bookings_space_id,\
                                                    bookings.owner_id AS bookings_owner_id,\
                                                    bookings.approved\
                                                    FROM users\
                                                    LEFT JOIN spaces ON spaces.owner_id = users.id\
                                                    LEFT JOIN bookings ON bookings.space_id = spaces.id\
                                                    WHERE users.id = %s\
                                                    ORDER BY spaces.id ASC, bookings.id ASC', [user_id])
                                                # FROM users LEFT JOIN bookings ON bookings.owner_id = users.id LEFT JOIN spaces ON spaces.id = bookings.space_id WHERE users.id = %s ORDER BY spaces.id ASC, bookings.id ASC', [user_id])
        return self._process_information(user_information)
    
    def find_all_information_as_guest(self, user_id):
        user_information = self._connection.execute('SELECT\
                                                    users.id AS owner_id,\
                                                    users.username,\
                                                    users.name AS name,\
                                                    users.email,\
                                                    users.phone_number,\
                                                    spaces.id AS space_id,\
                                                    spaces.name AS space_name,\
                                                    spaces.address,\
                                                    spaces.description,\
                                                    spaces.price,\
                                                    spaces.dates_booked,\
                                                    spaces.owner_id AS space_owner_id,\
                                                    bookings.id AS booking_id,\
                                                    bookings.check_in,\
                                                    bookings.check_out,\
                                                    bookings.user_id AS user_id,\
                                                    bookings.space_id AS bookings_space_id,\
                                                    bookings.owner_id AS bookings_owner_id,\
                                                    bookings.approved\
                                                    FROM users\
                                                    LEFT JOIN bookings ON bookings.user_id = users.id\
                                                    LEFT JOIN spaces ON spaces.id = bookings.space_id\
                                                    WHERE users.id = %s\
                                                    ORDER BY spaces.id ASC, bookings.id ASC', [user_id])
                                                    # FROM users LEFT JOIN bookings ON bookings.user_id = users.id LEFT JOIN spaces ON bookings.space_id = spaces.id WHERE users.id = %s ORDER BY spaces.id ASC, bookings.id ASC', [user_id])
    
        return self._process_information(user_information)
    
    def _process_information(self, user_information):
        if user_information[0]['space_id'] is None:

            user = User(user_information[0]['owner_id'], 
                user_information[0]['username'], 
                user_information[0]['name'], 
                None, 
                user_information[0]['email'], 
                user_information[0]['phone_number'], 
                [])
            return user
        
        bookings = []
        all_user_spaces = []
        space_ref = user_information[0]['space_id']
        for index, space in enumerate(user_information):
            if not space['space_id'] == space_ref:
                complete_space = Space(user_information[index - 1]['space_id'], user_information[index - 1]['space_name'], user_information[index - 1]['address'], user_information[index - 1]['description'], user_information[index - 1]['price'], user_information[index - 1]['dates_booked'], user_information[index - 1]['space_owner_id'], bookings)
                all_user_spaces.append(complete_space)
                bookings = []
                space_ref = space['space_id']
            if space['bookings_space_id'] == space['space_id']:

                total_price = calculate_total_price(space["price"], space["check_in"], space["check_out"])
                booking = Booking(space['booking_id'], space['check_in'], space['check_out'], space['user_id'], space['bookings_space_id'], space['bookings_owner_id'], total_price, space['approved'])

                bookings.append(booking)
        complete_space = Space(space['space_id'], space['space_name'], space['address'], space['description'], space['price'], space['dates_booked'], space['space_owner_id'], bookings)
        all_user_spaces.append(complete_space)
        user = User(user_information[0]['owner_id'], user_information[0]['username'], user_information[0]['name'], None, user_information[0]['email'], user_information[0]['phone_number'], all_user_spaces)
        return user

        