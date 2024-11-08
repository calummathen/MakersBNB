import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository

from dotenv import load_dotenv
from routes.routes import *
from dotenv import load_dotenv
from helper_functions import protect_route, location_filter


# Create a new Flask app
app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/home', methods=['GET'])
def get_index():
    logged_in = protect_route()
    if logged_in:
        return logged_in
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    location = request.args.get("location", '')
    if location != '':
        spaces = location_filter(spaces, location)
    return render_template('home.html', query=location, spaces=spaces)


auth_routes(app)
single_space_routes(app)
new_spaces_routes(app)
profile_pages_routes(app)
request_routes(app)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

