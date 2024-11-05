import os
from flask import Flask, request, render_template, session
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user import User
from lib.user_repository import UserRepository
from validation_methods import *

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'sample_key'

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/signup', methods=['GET'])
def get_root():
    connection = get_flask_database_connection(app)
    return render_template('signup.html')

@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    print(spaces)
    return render_template('home.html', spaces=spaces)

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


    
    

@app.route('/new_space', methods=['GET'])
def get_test_route():
    return render_template('space_form.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    name = request.form.get('name')
    email = request.form.get('email')
    phone_number = request.form.get('phone_number')
    username = request.form.get('username')
    password = request.form.get('password')
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    repository.create_user(User(None, username, name, password, email, phone_number))
    return str(repository.find_user(3))

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
