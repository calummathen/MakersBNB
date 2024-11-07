from lib.space import Space

def test_space_constructs(db_connection):
    space = Space(1, "Cezary", "123 Fake Street", "A nice space", 200.50, ["2024-11-01", "2024-11-02"], 1)
    assert space.id == 1
    assert space.name == "Cezary"
    assert space.address == "123 Fake Street"
    assert space.description == "A nice space"
    assert space.price == 200.50
    assert space.dates_booked == ["2024-11-01", "2024-11-02"]
    assert space.owner_id == 1
    assert space.bookings == []

def test_space_formats_nicely(db_connection):
    space = Space(1, "Cezary", "123 Fake Street", "A nice space", 200.50, ["2024-11-01", "2024-11-02"], 1)
    assert str(space) == "Space(1, Cezary, 123 Fake Street, A nice space, 200.50, ['2024-11-01', '2024-11-02'], 1, [])"

def test_spaces_are_equal(db_connection):
    space1 = Space(1, "Cezary", "123 Fake Street", "A nice space", 200.50, ['2024-11-01', '2024-11-02'], 1)
    space2 = Space(1, "Cezary", "123 Fake Street", "A nice space", 200.50, ['2024-11-01', '2024-11-02'], 1)
    assert space1 == space2