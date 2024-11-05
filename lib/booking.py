class Booking():
    def __init__(self, booking_id, check_in, check_out, user_id, space_id):
        self.booking_id = booking_id
        self.check_in = check_in
        self.check_out = check_out
        self.user_id = user_id
        self.space_id = space_id
        
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    
    def __repr__(self):
        return f"Booking({self.booking_id}, {self.check_in}, {self.check_out}, {self.user_id}, {self.space_id})"