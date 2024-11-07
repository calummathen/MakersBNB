DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;



CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    check_in DATE,
    check_out DATE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    space_id INTEGER REFERENCES spaces(id) ON DELETE CASCADE ON UPDATE CASCADE,
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    total_price FLOAT,
    approved BOOLEAN
);


INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES('2024-12-01', '2024-12-07', 1, 1, 1, 100, TRUE);
INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES('2024-12-07', '2024-12-12', 2, 1, 1, 200, TRUE);
INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES('2024-12-16', '2024-12-20', 1, 1, 1, 300, FALSE);
INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES('2024-12-22', '2024-12-23', 2, 1, 1, 400, TRUE);
INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES('2024-12-26', '2025-01-01', 1, 1, 1, 500, FALSE);
INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, total_price, approved) VALUES('2024-12-26', '2025-01-01', 2, 2, 1, 600, TRUE);