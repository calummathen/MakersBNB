from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.user import User
from lib.user_repository import UserRepository
from datetime import *

# Check we can use stored booking information to get stored user and space information:

# Currently this test does nothing as it is unfinished:

def test_booking_links_space_and_user(db_connection):
    pass
    # db_connection.seed("seeds/spaces.sql")
    # db_connection.seed("seeds/bookings.sql")
    # space_repository = SpaceRepository(db_connection)
    # user_repository = UserRepository(db_connection)
    # booking_repository = BookingRepository(db_connection)
    # # Create a user and a space
    # user_repository.create_user(User(None, 'test_username', 'Test Name', 'test_password', 'testemail@example.com', '07777626666')) # 4th user
    # space_repository.create(Space(None,'Property Name','22 Example Street','example description',100.00,'[2024-10-15, 2024-10-16, 2024-10-17]', 4)) # 5th space
    # booking_repository.create_booking(Booking(None, datetime.strptime('2024-10-18', '%Y-%m-%d').date(), datetime.strptime('2024-10-20', '%Y-%m-%d').date(), 5, 4, True)) #7th booking
    # # We can use the booking id to get the ids for a space and a user and get the space and user's information:
    # returned_booking = booking_repository.find_booking(7)
    


