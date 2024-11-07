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
from helper_functions import protect_route, calculate_total_price


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
    space_repository = SpaceRepository(connection)
    space = space_repository.find(space_id)
    price_per_night = space.price
    total_price = calculate_total_price(price_per_night, check_in, check_out)
    owner_id = space.owner_id
    new_booking = Booking(None, check_in, check_out, user_id, space_id, owner_id, total_price)
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


@app.route('/new_space', methods=['GET'])
def get_test_route():
    return render_template('space_form.html')


# @app.route('/signup', methods=['POST'])
# def create_user():
#     name = str(request.form.get('name'))
#     print(name)
#     email = str(request.form.get('email'))
#     phone_number = str(request.form.get('phone_number'))
#     username = str(request.form.get('username'))
#     password = str(request.form.get('password'))
#     errors = [error for error in check_signup_valid(name, email, phone_number, username, password) if error != True]
#     if len(errors) != 0:
#         return render_template('signup.html', errors=errors)
#     else:
#         connection = get_flask_database_connection(app)
#         repository = UserRepository(connection)
#         repository.create_user(User(None, username, name, password, email, phone_number))
#         # return f'{str(repository.find_user(3))} \n SHOULD RETURN TO login.html - this is temporary'
#         return render_template('login.html',account_created=True)

@app.route('/requests', methods=['GET'])
def booking_requests():
    username = session['username']
    user_id = session['id']
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    users_bookings = booking_repository.find_booking_for_user(user_id)
    space_repository = SpaceRepository(connection)
    user_repository = UserRepository(connection)
    
    
    booking_information_list = []
    for booking in users_bookings:
        booking_information = {}
        booking_information["check_in"] = booking.check_in
        booking_information["check_out"] = booking.check_out
        booking_information["approved"] = booking.approved
        booking_information["space_name"] = space_repository.find(booking.space_id).name
        booking_information["booking_id"] = booking.booking_id
        booking_information_list.append(booking_information)
    
    
    all_bookings_for_each_space_for_owner = []
    owners_spaces = space_repository.all_for_owner(user_id)
    for space in owners_spaces:
        all_bookings_for_a_space = {}
        bookings_for_space = booking_repository.find_booking_for_space(space.id)

        if bookings_for_space != []:
            all_required_info_for_all_bookings = []
            for booking in bookings_for_space:
                space_name = space_repository.find(booking.space_id).name
                all_required_info_for_a_booking = {}
                user_for_this_booking = user_repository.find_user(booking.user_id)
                all_required_info_for_a_booking["username"] = user_for_this_booking.username
                all_required_info_for_a_booking["user_id"] = user_for_this_booking.id
                all_required_info_for_a_booking["check_in"] = booking.check_in
                all_required_info_for_a_booking["check_out"] = booking.check_out
                all_required_info_for_a_booking["approved"] = booking.approved
                all_required_info_for_a_booking["booking_id"] = booking.booking_id
                all_required_info_for_all_bookings.append(all_required_info_for_a_booking)        
            all_bookings_for_a_space[space_name] = all_required_info_for_all_bookings
            all_bookings_for_each_space_for_owner.append(all_bookings_for_a_space)

    return render_template('requests.html', user_id=user_id, username=username, booking_information_list=booking_information_list, all_bookings_for_each_space_for_owner=all_bookings_for_each_space_for_owner)
    

@app.route('/requests/owner/<int:request_id>', methods=['GET'])
def owners_booking_request(request_id):
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking = booking_repository.find_booking(request_id)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(booking.space_id)
    user_repository = UserRepository(connection)
    username = user_repository.find_user(booking.user_id).username
    space_name = space_repository.find(booking.space_id).name
    if space.owner_id != session['id']:
        return '', 403
    print(booking.booking_id)
    return render_template('owner_request.html', booking=booking, username=username, space_name=space_name)

@app.route('/requests/user/<int:request_id>', methods=['GET'])
def user_booking_request(request_id):
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking = booking_repository.find_booking(request_id)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(booking.space_id)
    user_repository = UserRepository(connection)
    username = user_repository.find_user(booking.user_id).username
    space_name = space_repository.find(booking.space_id).name
    if booking.user_id != session['id']:
        return '', 403
    print(booking.booking_id)
    return render_template('user_request.html', booking=booking, username=username, space_name=space_name)

@app.route('/requests/approved', methods=['POST'])
def approve_booking():
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking_id = request.form["booking_id"]
    booking_repository.approved(booking_id)
    return redirect(url_for('booking_requests'))

@app.route('/requests/cancel', methods=['POST'])
def cancel_booking():
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking_id = request.form["booking_id"]
    booking_repository.delete_booking(booking_id)
    return redirect(url_for('booking_requests'))

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

