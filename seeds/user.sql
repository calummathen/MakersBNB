DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(16),
    name VARCHAR(30),
    password VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(11)
);


INSERT INTO users (username, name, password, email, phone_number) VALUES('username_1', 'name_1', 'password_1', 'email_1@gmail.com', '07777111111');
INSERT INTO users (username, name, password, email, phone_number) VALUES('username_2', 'name_2', 'password_2', 'email_2@gmail.com', '07777222222');