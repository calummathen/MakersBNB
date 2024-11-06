import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user import User
from lib.user_repository import UserRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from validation_methods import check_signup_valid
from dotenv import load_dotenv
from datetime import date
import json
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
@app.route('/', methods=['GET'])
def get_login_page():
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def get_root():
    return render_template('signup.html',errors=[])

@app.route('/home', methods=['GET'])
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
    owner_info = repository.find_all_information_as_owner(id)
    guest_info = repository.find_all_information_as_guest(id)
    username = session['username']

    return render_template('profile.html', username=username, owner=owner_info, guest=guest_info)

@app.route('/profile/edit', methods=['GET'])
def edit_profile():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    id = session['id']
    user = repository.find_user(id)
    return render_template('edit_profile.html', user=user)

@app.route('/profile/edit', methods=['POST'])
def change_profile():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    id = session['id']
    # Unfortunately need to do this to get the password
    user = repository.find_user(id)
    print(user.password)
    repository.update_user(User(id, username, name, user.password, email, phone_number))
    return redirect(url_for('profile'))

from authentication_routes import auth_routes
auth_routes(app)


@app.route('/space/<int:id>', methods=['GET'])
def display_single_space(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(id)
    booking_repository = BookingRepository(connection)
    current_bookings = booking_repository.find_booking_for_space(id)
    unavailable_dates = []
    for booking in current_bookings:
        dates = {
            "from": booking.check_in.strftime('%Y-%m-%d'),
            "to": booking.check_out.strftime('%Y-%m-%d')
        }
        unavailable_dates.append(dates)

    return render_template('single_space.html', space=space, unavailable_dates=unavailable_dates)
    

# Route for Signing up
# Commented out as don't believe it is needed anymore, but want to check:


@app.route('/new_space', methods=['GET'])
def get_test_route():
    return render_template('space_form.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

