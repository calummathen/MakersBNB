from lib.booking import Booking
from lib.space_repository import SpaceRepository


class BookingRepository():
    def __init__(self, connection):
        self.__connection = connection
        
        
    def find_booking_for_space(self, space_id, approved_only=None):
        if approved_only == None:
            results = self.__connection.execute("SELECT * FROM bookings WHERE space_id = %s", [space_id])
        elif type(approved_only) == bool:
            results = self.__connection.execute("SELECT * FROM bookings WHERE space_id = %s and approved = %s", [space_id, approved_only])
        list_of_bookings = [Booking(result["id"], 
                                    result["check_in"],
                                    result["check_out"],
                                    result["user_id"],
                                    result["space_id"],
                                    result['owner_id'],
                                    result["total_price"],
                                    result["approved"]) for result in results]
        return list_of_bookings
    
    
    def find_booking_for_user(self, user_id, approved_only=None):
        if approved_only == None:
            results = self.__connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        elif type(approved_only) == bool:
            results = self.__connection.execute("SELECT * FROM bookings WHERE user_id = %s and approved = %s", [user_id, approved_only])
        list_of_bookings = [Booking(result["id"], 
                                    result["check_in"],
                                    result["check_out"],
                                    result["user_id"],
                                    result["space_id"],
                                    result['owner_id'],
                                    result["total_price"],
                                    result["approved"]) for result in results]
        return list_of_bookings
    
    
    def find_booking(self, id):
        try:
            result = self.__connection.execute("SELECT * FROM bookings WHERE id = %s", [id])[0]
        except IndexError:
            return None
        booking = Booking(result["id"], 
                                    result["check_in"],
                                    result["check_out"],
                                    result["user_id"],
                                    result["space_id"],
                                    result['owner_id'],
                                    result["total_price"],
                                    result["approved"])
        return booking
    
    
    def create_booking(self, booking):
        self.__connection.execute("INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES(%s, %s, %s, %s, %s, %s, %s)", [booking.check_in, booking.check_out, booking.user_id, booking.space_id, booking.owner_id, booking.total_price, booking.approved])
    
    
    def delete_booking(self, id):
        self.__connection.execute("DELETE FROM bookings WHERE id = %s", [id])
        
        
    def approved(self, id):
        self.__connection.execute("UPDATE bookings SET approved = TRUE WHERE id = %s", [id])
        
        
    def is_valid_booking(self, new_booking):
        # this code is extremely hard to understand, trust us, it works
        # if the booking you want to make conflicts with an existing booking, method returns false, its not valid
        booking_list = self.find_booking_for_space(new_booking.space_id)
        for booking in booking_list:
            if booking.check_in < new_booking.check_out and booking.check_out > new_booking.check_in:
                return False
        return True


