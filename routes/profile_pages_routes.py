from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session, redirect, url_for
from lib.user_repository import UserRepository
from lib.user import User
from helper_functions import protect_route
from validation_methods import check_profile_update_valid

def profile_pages_routes(app):
    @app.route('/profile', methods=['GET'])
    def profile():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        id = session['id']
        owner_info = repository.find_all_information_as_owner(id)
        guest_info = repository.find_all_information_as_guest(id)
        username = session['username']
        return render_template('profile.html', username=username, owner=owner_info, guest=guest_info)
    
    @app.route('/profile/edit', methods=['GET'])
    def edit_profile():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        id = session['id']
        user = repository.find_user(id)
        return render_template('edit_profile.html', user=user)
    
    @app.route('/profile/edit', methods=['POST'])
    def change_profile():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        username = request.form['username']
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        id = session['id']
        user = repository.find_user(id)
        errors = [error for error in check_profile_update_valid(username, email, phone_number, name, user.username, user.email) if error != True]
        # Unfortunately need to do this to get the password
        user = repository.find_user(id)
        if len(errors) != 0:
            return render_template('edit_profile.html', user=user, errors=errors)
        else:
            repository.update_user(User(id, username, name, user.password, email, phone_number))
            session['username'] = username
            return redirect(url_for('profile'))