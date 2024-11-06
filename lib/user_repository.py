from lib.user import *
from werkzeug.security import check_password_hash, generate_password_hash
from lib.space import Space
from lib.booking import Booking

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
        hashed_password = generate_password_hash(user_to_update.password)
        self._connection.execute("UPDATE users SET username=%s, name=%s, password=%s, email=%s, phone_number=%s WHERE id = %s", 
        [user_to_update.username, user_to_update.name, hashed_password, user_to_update.email, user_to_update.phone_number, user_to_update.id])
        
    def delete_user(self, id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [id])

    def get_usernames_emails(self):
        result = self._connection.execute("SELECT username,email FROM users")
        return result
    
    def find_all_information(self, user_id):
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
                                                    bookings.id AS booking_id,\
                                                    bookings.check_in,\
                                                    bookings.check_out,\
                                                    bookings.user_id AS user_id,\
                                                    bookings.space_id AS bookings_space_id,\
                                                    bookings.approved\
                                                    FROM users JOIN spaces ON spaces.owner_id = users.id JOIN bookings ON bookings.owner_id = users.id WHERE users.id = %s ORDER BY spaces.id ASC', [user_id])
        if not user_information:
            return []
        
        bookings = []
        all_user_bookings = []
        all_user_spaces = []
        space_ref = user_information[0]['space_id']
        for index, space in enumerate(user_information):
            
            if not space['space_id'] == space_ref:
                complete_space = Space(user_information[index - 1]['space_id'], user_information[index - 1]['space_name'], user_information[index - 1]['address'], user_information[index - 1]['description'], user_information[index - 1]['price'], user_information[index - 1]['dates_booked'], user_information[index - 1]['owner_id'], bookings)
                all_user_spaces.append(complete_space)
                bookings = []
                space_ref = space['space_id']
            if space['bookings_space_id'] == space['space_id']:
                booking = Booking(space['booking_id'], space['check_in'], space['check_out'], space['user_id'], space['bookings_space_id'], space['owner_id'], space['approved'])
                bookings.append(booking)
                if space['user_id'] == space['owner_id']:
                    all_user_bookings.append(booking)
            
        complete_space = Space(space['space_id'], space['space_name'], space['address'], space['description'], space['price'], space['dates_booked'], space['owner_id'], bookings)
        all_user_spaces.append(complete_space)
        user = User(user_information[0]['owner_id'], user_information[0]['username'], user_information[0]['name'], None, user_information[0]['email'], user_information[0]['phone_number'], all_user_spaces, all_user_bookings)
        return user