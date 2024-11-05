from lib.user import *
from werkzeug.security import check_password_hash, generate_password_hash

class UserRepository:
    def __init__(self, connection):
        self._connection = connection


    def login(self, username, password):
        attempted_user = self._connection.execute('SELECT * FROM users WHERE username = %s', [username])
        if len(attempted_user) == 0:
            return False
        user = attempted_user[0]
        correct_password = user['password'] == password
        # correct_password = check_password_hash(user['password'], password)
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
        # hashed_password = generate_password_hash(user_to_add.password)
        self._connection.execute("INSERT INTO users (username, name, password, email, phone_number) VALUES(%s, %s, %s, %s, %s)", 
        [user_to_add.username, user_to_add.name, user_to_add.password, user_to_add.email, user_to_add.phone_number]
        )
        
    def update_user(self, user_to_update):
        self._connection.execute("UPDATE users SET username=%s, name=%s, password=%s, email=%s, phone_number=%s", 
        [user_to_update.username, user_to_update.name, user_to_update.password, user_to_update.email, user_to_update.phone_number])
        
    def delete_user(self, id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [id])