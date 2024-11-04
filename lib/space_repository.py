from lib.space import Space

class SpaceRepository():
    def __init__(self, db_connection):
        self._connection = db_connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces ORDER BY id asc')
        print(rows)
        spaces = [Space(space['id'], space['name'], space['address'], space['description'],
                        space['price'], space['dates_booked'], space['owner_id']) for space in rows]
        return spaces
