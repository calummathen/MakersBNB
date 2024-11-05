from lib.booking import Booking

class BookingRepository():
    def __init__(self, connection):
        self.__connection = connection
        
        
    def find_booking_for_space(self, space_id):
        results = self.__connection.execute("SELECT * FROM bookings WHERE space_id = %s", [space_id])
        print(type(results[0]["check_in"]))
        list_of_bookings = [Booking(result["id"], 
                                    result["check_in"],
                                    result["check_out"],
                                    result["user_id"],
                                    result["space_id"]) for result in results]
        return list_of_bookings