from lib.database_connection import get_flask_database_connection
from flask import request, render_template, session, redirect, url_for
from lib.space_repository import SpaceRepository
from lib.space import Space
from helper_functions import protect_route
from validation_methods import check_space_creation_valid

def new_spaces_routes(app):
    @app.route('/space/new', methods=['GET'])
    def get_new_space_form():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        return render_template('space_form.html')

    @app.route('/space/new', methods=['POST'])
    def create_new_space():
        logged_in = protect_route()
        if logged_in:
            return logged_in
        connection = get_flask_database_connection(app)
        space_repository = SpaceRepository(connection)
        name = request.form['name']
        address = request.form['address']
        description = request.form['description']
        price = request.form['price']
        id = session['id']
        errors = [error for error in check_space_creation_valid(name,address,description,price) if error != True]
        if len(errors) != 0:
            return render_template('space_form.html', errors=errors)
        else:
            space = Space(None, name, address, description, price, '[]', id)
            space_repository.create(space)
            return redirect(url_for('profile'))