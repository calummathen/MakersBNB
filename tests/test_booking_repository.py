from lib.booking_repository import *
from lib.booking import *
from datetime import *


def test_get_all_bookings_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_space(1)
    booking_1 = Booking(1, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-07', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    booking_2 = Booking(2, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 2, 1, 1, 200,  True)
    booking_3 = Booking(3, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 300,  False)
    booking_4 = Booking(4, datetime.strptime('2024-12-22', '%Y-%m-%d').date(), datetime.strptime('2024-12-23', '%Y-%m-%d').date(), 2, 1, 1, 400, True)
    booking_5 = Booking(5, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 1, 1, 1, 500, False)
    assert booking_list == [
        booking_1,
        booking_2,
        booking_3,
        booking_4,
        booking_5
    ]
    
    
def test_get_all_bookings_for_space_1_if_approved(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_space(1, True)
    booking_1 = Booking(1, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-07', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    booking_2 = Booking(2, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 2, 1, 1, 200, True)
    booking_4 = Booking(4, datetime.strptime('2024-12-22', '%Y-%m-%d').date(), datetime.strptime('2024-12-23', '%Y-%m-%d').date(), 2, 1, 1, 400, True)
    assert booking_list == [
        booking_1,
        booking_2,
        booking_4
    ]
    
    
def test_get_all_bookings_for_space_1_if_not_approved(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_space(1, False)
    booking_3 = Booking(3, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 300, False)
    booking_5 = Booking(5, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 1, 1, 1, 500, False)
    assert booking_list == [
        booking_3,
        booking_5
    ]
    
    
    

def test_get_all_bookings_for_user_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_user(1)
    booking_1 = Booking(1, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-07', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    booking_3 = Booking(3, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 300, False)
    booking_5 = Booking(5, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 1, 1, 1, 500, False)
    assert booking_list == [
        booking_1,
        booking_3,
        booking_5
    ]
    
    
def test_get_all_bookings_for_user_1_if_approved(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_user(1, True)
    booking_1 = Booking(1, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-07', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    assert booking_list == [
        booking_1
    ]
    
    
def test_get_all_bookings_for_user_1_if_not_approved(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_user(1, False)
    booking_3 = Booking(3, datetime.strptime('2024-12-16', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 300, False)
    booking_5 = Booking(5, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 1, 1, 1, 500, False)
    assert booking_list == [
        booking_3,
        booking_5
    ]
    
def test_get_all_bookings_for_user_2(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_user(2)
    booking_2 = Booking(2, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 2, 1, 1, 200, True)
    booking_4 = Booking(4, datetime.strptime('2024-12-22', '%Y-%m-%d').date(), datetime.strptime('2024-12-23', '%Y-%m-%d').date(), 2, 1, 1, 400, True)
    booking_6 = Booking(6, datetime.strptime('2024-12-26', '%Y-%m-%d').date(), datetime.strptime('2025-01-01', '%Y-%m-%d').date(), 2, 2, 1, 600, True)
    assert booking_list == [
        booking_2,
        booking_4,
        booking_6
    ]
    
    
def test_get_single_booking(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_result = repository.find_booking(2)
    booking_2 = Booking(2, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-12', '%Y-%m-%d').date(), 2, 1, 1, 200, True)
    assert booking_result == booking_2
    
    
def test_get_single_booking_doesnt_exist(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_result = repository.find_booking(10)
    assert booking_result == None
    
    
def test_create_new_booking(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    created_booking = Booking(7, datetime.strptime('2025-01-02', '%Y-%m-%d').date(), datetime.strptime('2025-01-05', '%Y-%m-%d').date(), 1, 1, 1, 700, True)
    repository.create_booking(created_booking)
    booking = repository.find_booking(7)
    assert booking == created_booking
    
    
def test_delete_booking(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    repository.delete_booking(6)
    booking = repository.find_booking(6)
    assert booking == None
    
    
def test_approved(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    repository.approved(3)
    booking = repository.find_booking(3)
    assert booking.approved == True
    
    
def test_is_valid_booking_where_existing_booking_has_same_dates_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-08', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == False
    
def test_is_valid_booking_where_check_out_is_in_existing_booking_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-06', '%Y-%m-%d').date(), datetime.strptime('2024-12-11', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == False
    
def test_is_valid_booking_where_existing_booking_within_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-06', '%Y-%m-%d').date(), datetime.strptime('2024-12-13', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == False
    
    
def test_is_valid_booking_where_check_in_is_in_existing_booking_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-08', '%Y-%m-%d').date(), datetime.strptime('2024-12-13', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == False
    
    
def test_is_valid_booking_where_two_existing_bookings_exist_within_booking_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-07', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == False
    
    
def test_is_valid_booking_for_available_date_for_space_1(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-12', '%Y-%m-%d').date(), datetime.strptime('2024-12-16', '%Y-%m-%d').date(), 1, 1, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == True
    
def test_is_valid_booking_for_available_date_for_space_2(db_connection):
    db_connection.seed("seeds/spaces.sql")
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    potential_booking = Booking(None, datetime.strptime('2024-12-01', '%Y-%m-%d').date(), datetime.strptime('2024-12-20', '%Y-%m-%d').date(), 1, 2, 1, 100, True)
    is_valid_booking = repository.is_valid_booking(potential_booking)
    assert is_valid_booking == True
    
    