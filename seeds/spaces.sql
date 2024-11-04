DROP TABLE IF EXISTS spaces;

DROP SEQUENCE IF EXISTS spaces_id_seq;

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    address VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL,
    dates_booked VARCHAR(255),
    owner_id INTEGER
);

INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Big Hotel','4 Street','Dangerous area',150.99,'[]', 2);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Small House','5 street','Peterborough',00.00,'[]', 3);
