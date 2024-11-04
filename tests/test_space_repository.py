from lib.space_repository import SpaceRepository
from lib.space import Space

'''
Testing SpaceRepository #all
returns all spaces
'''
def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    result = repository.all()
    assert result == [
        Space(1,'Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1),
        Space(3, 'Big Hotel','4 Street','Dangerous area',150.99,'[]', 2),
        Space(4, 'Small House','5 street','Peterborough',00.00,'[]', 3)
    ]


