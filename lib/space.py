class Space:
    
    def __init__(self, id, name, address, description, price, dates_booked, owner_id):
        self.id = id
        self.name = name
        self.address = address
        self. description = description
        self.price = price
        self.dates_booked = dates_booked
        self.owner_id = owner_id

    def __repr__(self):
        return f"Space({self.id}, {self.name}, {self.address}, {self.description}, {self.price}, {self.dates_booked}, {self.owner_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__