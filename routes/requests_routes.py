from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session, redirect, url_for
from lib.booking_repository import BookingRepository
from lib.space_repository import SpaceRepository
from lib.user_repository import UserRepository
from helper_functions import protect_route

def request_routes(app):
    @app.route('/requests', methods=['GET'])
    def booking_requests():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        username = session['username']
        user_id = session['id']
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        users_bookings = booking_repository.find_booking_for_user(user_id, False)
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
            booking_information["total_price"] = f"{booking.total_price:.2f}"
            booking_information_list.append(booking_information)


        all_bookings_for_each_space_for_owner = []
        owners_spaces = space_repository.all_for_owner(user_id)
        for space in owners_spaces:
            all_bookings_for_a_space = {}
            bookings_for_space = booking_repository.find_booking_for_space(space.id, False)

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
                    all_required_info_for_a_booking["total_price"] = f"{booking.total_price:.2f}"
                    all_required_info_for_all_bookings.append(all_required_info_for_a_booking)        
                all_bookings_for_a_space[space_name] = all_required_info_for_all_bookings
                all_bookings_for_each_space_for_owner.append(all_bookings_for_a_space)

        return render_template('requests.html', user_id=user_id, username=username, booking_information_list=booking_information_list, all_bookings_for_each_space_for_owner=all_bookings_for_each_space_for_owner)


    @app.route('/requests/owner/<int:request_id>', methods=['GET'])
    def owners_booking_request(request_id):
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        booking = booking_repository.find_booking(request_id)
        space_repository = SpaceRepository(connection)
        space = space_repository.find(booking.space_id)
        user_repository = UserRepository(connection)
        username = user_repository.find_user(booking.user_id).username
        space_name = space_repository.find(booking.space_id).name
        booking.total_price = f"{booking.total_price:.2f}"
        if space.owner_id != session['id']:
            return '', 403
        print(booking.booking_id)
        return render_template('owner_request.html', booking=booking, username=username, space_name=space_name)

    @app.route('/requests/user/<int:request_id>', methods=['GET'])
    def user_booking_request(request_id):
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        booking = booking_repository.find_booking(request_id)
        space_repository = SpaceRepository(connection)
        space = space_repository.find(booking.space_id)
        user_repository = UserRepository(connection)
        username = user_repository.find_user(booking.user_id).username
        space_name = space_repository.find(booking.space_id).name
        booking.total_price = f"{booking.total_price:.2f}"
        if booking.user_id != session['id']:
            return '', 403
        print(booking.booking_id)
        return render_template('user_request.html', booking=booking, username=username, space_name=space_name)

    @app.route('/requests/approved', methods=['POST'])
    def approve_booking():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        booking_id = request.form["booking_id"]
        booking_repository.approved(booking_id)
        return redirect(url_for('booking_requests'))

    @app.route('/requests/cancel', methods=['POST'])
    def cancel_booking():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        booking_repository = BookingRepository(connection)
        booking_id = request.form["booking_id"]
        booking_repository.delete_booking(booking_id)
        return redirect(url_for('booking_requests'))