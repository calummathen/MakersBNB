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

'''
Testing SpaceRepository #find
returns specific space
'''
def test_find_specific_space(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    result = repository.find(2)
    assert result == Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1)

'''
Testing SpaceRepository #create
creates new space, adds to table spaces
'''
def test_create_space(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    repository.create(Space(None,'Igloo','23 Example Street','Cold neighbourhood',100.00,'[2024-10-15, 2024-10-16, 2024-10-17]', 3))
    result = repository.all()
    assert result == [
        Space(1,'Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1),
        Space(3, 'Big Hotel','4 Street','Dangerous area',150.99,'[]', 2),
        Space(4, 'Small House','5 street','Peterborough',00.00,'[]', 3),
        Space(5,'Igloo','23 Example Street','Cold neighbourhood',100.00,'[2024-10-15, 2024-10-16, 2024-10-17]', 3)
    ]

'''
Testing SpaceRepository #update
updates an existing space with new information
'''
def test_update_space(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    repository.update(Space(1,'Stratfest','Wembley','Company event party',1200.50,'[2024-09-15, 2024-09-16]', 1))
    result = repository.all()
    assert result == [
        Space(1,'Stratfest','Wembley','Company event party',1200.50,'[2024-09-15, 2024-09-16]', 1),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1),
        Space(3, 'Big Hotel','4 Street','Dangerous area',150.99,'[]', 2),
        Space(4, 'Small House','5 street','Peterborough',00.00,'[]', 3)
    ]

'''
Testing SpaceRepository #delete
Deletes a space from the table spaces
'''
def test_delete_space(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    repository.delete(4)
    result = repository.all()
    assert result == [
        Space(1,'Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1),
        Space(3, 'Big Hotel','4 Street','Dangerous area',150.99,'[]', 2)
    ]
    
def test_get_all_spaces_for_owner_1(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    result = repository.all_for_owner(1)
    assert result == [
        Space(1,'Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1),
        Space(2, 'Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1)
    ]
    
    
def test_get_all_spaces_for_owner_2(db_connection):
    db_connection.seed('seeds/spaces.sql')
    repository = SpaceRepository(db_connection)
    result = repository.all_for_owner(2)
    assert result == [
        Space(3, 'Big Hotel','4 Street','Dangerous area',150.99,'[]', 2)
    ]

