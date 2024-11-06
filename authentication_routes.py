from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session
from lib.user import User
from lib.user_repository import UserRepository

def auth_routes(app):
    # Route for Signing up
    @app.route('/signup', methods=['POST'])
    def sign_up():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        id = request.form["id"]
        username = request.form["username"]
        name = request.form["name"]
        password = request.form["password"]
        email = request.form["email"]
        phone_number = request.form["phone_number"]
        # Will need a check for a unique user
        new_user = User(id, username, name, password, email, phone_number)
        repository.create_user(new_user)
        return render_template('login.html')

    @app.route('/login', methods=['POST'])
    def login():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        username = request.form["username"]
        password = request.form["password"]
        user = repository.login(username, password)
        if not user:
            error = 'Incorrect Username or Password'
            return error
            # return render_template('login.html', error=error)
        if 'username' not in session:
            session['id'] = user['id']
            session['username'] = user['username']
        return user

    @app.route('/logout')
    def logout():
        session.clear()
        return 'hello world'