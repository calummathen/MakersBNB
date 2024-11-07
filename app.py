import os
from flask import Flask, request, render_template, session, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.user import User
from lib.user_repository import UserRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from validation_methods import check_signup_valid
from dotenv import load_dotenv
from datetime import datetime, timedelta
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
    user = repository.find_with_space(id)
    
    

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
        check_in = booking.check_in
        check_out = booking.check_out
        dates = {
            "from": (check_in + timedelta(days=1)).strftime('%Y-%m-%d'),
            "to": (check_out - timedelta(days=1)).strftime('%Y-%m-%d')
        }
        unavailable_dates.append(dates)

    return render_template('single_space.html', space=space, unavailable_dates=unavailable_dates)

@app.route('/space/create_booking/<int:space_id>', methods=['POST'])
def create_booking(space_id):

    check_in = datetime.strptime(request.form.get('startDate'), "%Y-%m-%d").date()
    check_out = datetime.strptime(request.form.get('endDate'), "%Y-%m-%d").date()
    user_id = 1

    # print(check_in, check_out, user_id, space_id)

    connection = get_flask_database_connection(app)
    new_booking = Booking(None, check_in, check_out, user_id, space_id)
    # need to add user ID!!!!

    booking_repository = BookingRepository(connection)
    if booking_repository.is_valid_booking(new_booking):
        booking_repository.create_booking(new_booking)
        flash("Booking successfully created!", "success") 
        return redirect(url_for('display_single_space', id=space_id)) 
    else:
        flash("Invalid booking: The selected dates are not available.", "error")  # Flash error message
        return redirect(url_for('display_single_space', id=space_id))  # Redirect
    


    

# Route for Signing up
# Commented out as don't believe it is needed anymore, but want to check:
'''
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
'''





@app.route('/new_space', methods=['GET'])
def get_test_route():
    return render_template('space_form.html')


@app.route('/signup', methods=['POST'])
def create_user():
    name = str(request.form.get('name'))
    print(name)
    email = str(request.form.get('email'))
    phone_number = str(request.form.get('phone_number'))
    username = str(request.form.get('username'))
    password = str(request.form.get('password'))
    errors = [error for error in check_signup_valid(name, email, phone_number, username, password) if error != True]
    if len(errors) != 0:
        return render_template('signup.html', errors=errors)
    else:
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        repository.create_user(User(None, username, name, password, email, phone_number))
        # return f'{str(repository.find_user(3))} \n SHOULD RETURN TO login.html - this is temporary'
        return render_template('login.html',account_created=True)




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

