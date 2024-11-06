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

INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'username_1', 
    'name_1', 
    'scrypt:32768:8:1$n952oFWoS88c2UCd$b030f2524c51d45b866f128a92335d05d3be6ec27c0c153d4db9e58514ffbab4f4bea39d93694cfd5ae4eb2d51f6a10b866ae87057a7cd246f4eadf37576308d', 
    'email_1@gmail.com',
    '07777111111');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'username_2', 
    'name_2', 
    'scrypt:32768:8:1$lj6tuvqbfBTNIcMx$e8b2b2fe230d39e1f2afc1b07efcf578ee3a5fca9d0fe86d54f0ed8a7fb8118e1330edccac8d317069ed944a4d55f8ca56a14bcf13734d43aae9eff172080dc1', 
    'email_2@gmail.com', 
    '07777222222');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'username_3',
    'name_3', 
    'scrypt:32768:8:1$4gQwh0IBZhJT1zfR$c982b4bb7302984ec2d00c94543f6f76c4d7fd1dbdbb54a1a3c80e7950dd123c73243f1e9f61df48d0462840ed3991b32b0d5580d2cd117baf1d7575fda5887e', 
    'email_3@gmail.com', 
    '07777333333');

INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Big Hotel','4 Street','Dangerous area',150.99,'[]', 2);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES ('Small House','5 street','Peterborough',00.00,'[]', 3);
