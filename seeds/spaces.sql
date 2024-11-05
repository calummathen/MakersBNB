DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(16) UNIQUE,
    name VARCHAR(30),
    password VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    phone_number VARCHAR(11) UNIQUE
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    address VARCHAR(255),
    description VARCHAR(255),
    price FLOAT,
    dates_booked VARCHAR(255),
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO users (username, name, password, email, phone_number) VALUES('username_1', 'name_1', 'password_1', 'email_1@gmail.com', '07777111111');
INSERT INTO users (username, name, password, email, phone_number) VALUES('username_2', 'name_2', 'password_2', 'email_2@gmail.com', '07777222222');
INSERT INTO users (username, name, password, email, phone_number) VALUES('username_3', 'name_3', 'password_3', 'email_3@gmail.com', '07777333333');

INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Big Hotel','4 Street','Dangerous area',150.99,'[]', 2);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Small House','5 street','Peterborough',00.00,'[]', 3);
