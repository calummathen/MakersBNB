import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space_repository import SpaceRepository
from lib.space import Space

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    print(spaces)
    return render_template('home.html', spaces=spaces)

@app.route('/new_space', methods=['GET'])
def get_test_route():
    
    return render_template('space_form.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
