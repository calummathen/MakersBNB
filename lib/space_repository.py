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
        
        
    def all_for_owner(self, owner_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE owner_id = %s ORDER BY id asc', [owner_id])
        spaces = [Space(space['id'], space['name'], space['address'], space['description'],
                        space['price'], space['dates_booked'], space['owner_id']) for space in rows]
        return spaces

