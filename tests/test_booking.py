from lib.booking import *

def test_initialise_booking():
    booking_id = 1
    check_in = "2024-12-12"
    check_out = "2024-12-18"
    user_id = 10
    space_id = 15
    owner_id = 2
    total_price = 100
    booking = Booking(booking_id, check_in, check_out, user_id, space_id, owner_id, total_price)
    assert booking.booking_id == booking_id
    assert booking.check_in == check_in
    assert booking.check_out == check_out
    assert booking.user_id == user_id
    assert booking.space_id == space_id
    assert booking.approved == False
    assert booking.owner_id == owner_id
    assert booking.total_price == 100


def test_compare_two_booking_with_same_details():
    booking_id = 1
    check_in = "2024-12-12"
    check_out = "2024-12-18"
    user_id = 10
    space_id = 15
    owner_id = 2
    total_price = 100
    booking = Booking(booking_id, check_in, check_out, user_id, space_id, owner_id, total_price)
    comparison_booking = Booking(booking_id, check_in, check_out, user_id, space_id, owner_id, total_price)
    assert booking == comparison_booking


def test_string_representation_of_booking():
    booking_id = 1
    check_in = "2024-12-12"
    check_out = "2024-12-18"
    user_id = 10
    space_id = 15
    owner_id = 2
    total_price = 100
    booking = Booking(booking_id, check_in, check_out, user_id, space_id, owner_id, total_price)
    booking_string = str(booking)
    assert booking_string == "Booking(1, 2024-12-12, 2024-12-18, 10, 15, 2, 100.00, False)"
