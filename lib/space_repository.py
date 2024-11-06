from lib.space import Space
from lib.booking import Booking

class SpaceRepository():
    def __init__(self, db_connection):
        self._connection = db_connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces ORDER BY id asc')
        spaces = [Space(space['id'], space['name'], space['address'], space['description'],
                        space['price'], space['dates_booked'], space['owner_id']) for space in rows]
        return spaces

    def find(self, space_id):
        space = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])[0]
        return Space(space['id'], space['name'], space['address'], space['description'],
                        space['price'], space['dates_booked'], space['owner_id'])
    
    def create(self, new_space):
        self._connection.execute('INSERT INTO spaces (name,address,description,price,dates_booked,owner_id) VALUES (%s,%s,%s,%s,%s,%s)',
                                [new_space.name, new_space.address, new_space.description, new_space.price, new_space.dates_booked, new_space.owner_id])
    
    def update(self, new_space):
        self._connection.execute('UPDATE spaces SET name=%s,address=%s,description=%s,price=%s,dates_booked=%s WHERE id = %s' ,
                                [new_space.name, new_space.address, new_space.description, new_space.price, new_space.dates_booked, new_space.id])
        
    def delete(self, space_id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s',[space_id])

    # def find_all_user_info(self, user_id):
    #     spaces = self._connection.execute('SELECT \
    #                                         bookings.id AS bookings_id,\
    #                                         bookings.check_in,\
    #                                         bookings.check_out,\
    #                                         bookings.user_id,\
    #                                         bookings.approved,\
    #                                         spaces.id AS space_id,\
    #                                         spaces.name,\
    #                                         spaces.address,\
    #                                         spaces.description,\
    #                                         spaces.price,\
    #                                         spaces.dates_booked,\
    #                                         spaces.owner_id\
    #                                         FROM spaces JOIN bookings ON bookings.space_id = spaces.id WHERE user_id = %s ORDER BY spaces.id asc', [user_id])
    #     if not spaces:
    #         return []
        
    #     bookings = []
    #     all_user_spaces = []
    #     space_ref = spaces[0]['space_id']
    #     for space in spaces:
            
    #         if not space['space_id'] == space_ref:
    #             print(bookings)
    #             complete_space = Space(space['space_id'], space['name'], space['address'], space['price'], space['dates_booked'], space['owner_id'], bookings)
    #             all_user_spaces.append(complete_space)
    #             bookings = []
    #             space_ref = space['space_id']
    #         booking = Booking(space['bookings_id'], space['check_in'], space['check_out'], space['user_id'], space['space_id'], space['owner_id'], space['approved'])
            
    #         bookings.append(booking)
    #     complete_space = Space(space['space_id'], space['name'], space['address'], space['description'], space['price'], space['dates_booked'], space['owner_id'], bookings)
    #     print(complete_space)
    #     all_user_spaces.append(complete_space)

    #     return all_user_spaces