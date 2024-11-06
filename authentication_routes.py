from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session, redirect
from lib.user import User
from lib.user_repository import UserRepository
from validation_methods import check_email_is_valid, check_signup_valid

def auth_routes(app):
    @app.route('/signup', methods=['POST'])
    def sign_up():
        name = request.form.get('name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        username = request.form.get('username')
        password = request.form.get('password')
        errors = [error for error in check_signup_valid(name, email, phone_number, username, password) if error != True]
        if len(errors) != 0:
            return render_template('signup.html', errors=errors)
        else:
            connection = get_flask_database_connection(app)
            repository = UserRepository(connection)
            repository.create_user(User(None, username, name, password, email, phone_number))
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
        # return user
        return redirect('/home', code=200)

    @app.route('/logout')
    def logout():
        session.clear()
        return 'hello world'