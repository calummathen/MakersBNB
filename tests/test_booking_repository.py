from lib.booking_repository import *
from lib.booking import *


def test_get_all_bookings_for_space_1(db_connection):
    db_connection.seed("seeds/bookings.sql")
    repository = BookingRepository(db_connection)
    booking_list = repository.find_booking_for_space(1)
    booking_1 = Booking(1, '2024-12-01', '2024-12-07', 1, 1)
    booking_2 = Booking(2, '2024-12-07', '2024-12-12', 2, 1)
    booking_3 = Booking(3, '2024-12-16', '2024-12-20', 1, 1)
    booking_4 = Booking(4, '2024-12-22', '2024-12-23', 2, 1)
    booking_5 = Booking(5, '2024-12-26', '2025-01-01', 1, 1)
    assert booking_list == [
        booking_1,
        booking_2,
        booking_3,
        booking_4,
        booking_5
    ]
    