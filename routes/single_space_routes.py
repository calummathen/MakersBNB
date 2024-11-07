from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session, redirect, url_for, flash
from lib.space_repository import SpaceRepository
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from helper_functions import calculate_total_price
from datetime import datetime, timedelta
from helper_functions import protect_route

def single_space_routes(app):
    @app.route('/space/<int:id>', methods=['GET'])
    def display_single_space(id):
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
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
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        # return f'{request.form.get('startDate')} and {request.form.get('endDate')}'
        if request.form.get('startDate') == '' or request.form.get('endDate') == 'undefined':
            flash("Please select a date range!", "error")
            return redirect(url_for('display_single_space', id=space_id)) 
        connection = get_flask_database_connection(app)
        check_in = datetime.strptime(request.form.get('startDate'), "%Y-%m-%d").date()
        check_out = datetime.strptime(request.form.get('endDate'), "%Y-%m-%d").date()
        print('test')
        print(check_in)
        print(check_out)
        user_id = session["id"]
        space_repository = SpaceRepository(connection)
        space = space_repository.find(space_id)
        price_per_night = space.price
        total_price = calculate_total_price(price_per_night, check_in, check_out)
        owner_id = space.owner_id
        new_booking = Booking(None, check_in, check_out, user_id, space_id, owner_id, total_price)


        booking_repository = BookingRepository(connection)

        if booking_repository.is_valid_booking(new_booking):
            booking_repository.create_booking(new_booking)
            return redirect(url_for('profile')) 
        else:
            flash("Invalid booking: The selected dates are not available.", "error")  # Flash error message
            return redirect(url_for('display_single_space', id=space_id))  # Redirect
