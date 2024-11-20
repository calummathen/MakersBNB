# MakersBnB Python Project

This web application allows users to list available spaces and book them for overnight stays of various lengths. It was developed as a group project using Python, Flask, HTML, CSS, and JavaScript, providing a robust platform for listing and hiring spaces with customisable availability and booking management.

## Features

### Core Functionality

User Signup & Authentication: Users can sign up, log in, and manage their profiles.
Listing Spaces: Any signed-up user can:
* List multiple spaces with a name, short description, and price per night.
* Manage their profile and update information
Booking Requests: Users can:
* Request to book a listed space for any available nights.
* Approve or deny booking requests for their spaces.
* Booked nights are automatically blocked to prevent double bookings.

### Real-Time Booking Management

* Availability Control: Spaces remain bookable until a booking request is confirmed.
* Booking Approvals: Space owners must approve booking requests before the booking is finalized.

### Technology Stack

* Backend: Python, Flask
* Frontend: HTML, CSS, JavaScript
* Database: PostgreSQL 


### Installation and Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Create a test and development PostgreSQL database
(makersbnb-venv); createdb YOUR_PROJECT_NAME
(makersbnb-venv); createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```