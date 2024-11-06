import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user import User
from lib.user_repository import UserRepository
from validation_methods import check_signup_valid
from dotenv import load_dotenv
from helper_functions import protect_route


# Create a new Flask app
app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/signup', methods=['GET'])
def get_root():
    return render_template('signup.html',errors=[])

@app.route('/index', methods=['GET'])
def get_index():
    logged_in = protect_route()
    if logged_in:
        return logged_in
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('home.html', spaces=spaces)

@app.route('/profile')
def profile():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    id = session['id']
    user = repository.find_with_space(id)
    
    

from authentication_routes import auth_routes
auth_routes(app)

@app.route('/new_space', methods=['GET'])
def get_test_route():
    return render_template('space_form.html')





# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
