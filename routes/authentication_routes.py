from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session, redirect, url_for
from lib.user import User
from lib.user_repository import UserRepository
from validation_methods import check_signup_valid

def auth_routes(app):

    @app.route('/', methods=['GET'])
    def get_login_page(error=None):
        if error == None:
            return render_template('login.html')
        else:
            return render_template('login.html', error=error)

    @app.route('/signup', methods=['GET'])
    def get_root():
        return render_template('signup.html',errors=[])

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
            return render_template('login.html', error=error)
            # return render_template('login.html', error=error)
        if 'username' not in session or 'username' in session != username:
            session['id'] = user['id']
            session['username'] = user['username']
        return redirect('/home')


    @app.route('/logout')
    def logout():
        session.clear()
        error = 'You have been signed out'
        return redirect(url_for('get_login_page'))
        # return redirect(url_for('get_login_page', error=error))
        # ^error being passed doesn't go anywhere, unsure how to change that