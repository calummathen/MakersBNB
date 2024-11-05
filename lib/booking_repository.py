from lib.booking import Booking

class BookingRepository():
    def __init__(self, connection):
        self.__connection = connection
        
        
    def find_booking_for_space(self, space_id):
        results = self.__connection.execute("SELECT * FROM bookings WHERE space_id = %s", [space_id])
        list_of_bookings = [Booking(result["id"], 
                                    result["check_in"],
                                    result["check_out"],
                                    result["user_id"],
                                    result["space_id"],
                                    result["approved"]) for result in results]
        return list_of_bookings
    
    
    def find_booking_for_user(self, user_id):
        results = self.__connection.execute("SELECT * FROM bookings WHERE user_id = %s", [user_id])
        list_of_bookings = [Booking(result["id"], 
                                    result["check_in"],
                                    result["check_out"],
                                    result["user_id"],
                                    result["space_id"],
                                    result["approved"]) for result in results]
        return list_of_bookings