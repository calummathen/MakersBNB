DROP TABLE IF EXISTS spaces CASCADE;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS bookings CASCADE;
DROP SEQUENCE IF EXISTS bookings_id_seq;

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


CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    check_in DATE,
    check_out DATE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    space_id INTEGER REFERENCES spaces(id) ON DELETE CASCADE ON UPDATE CASCADE,
    owner_id INTEGER REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE,
    approved BOOLEAN
);
    
INSERT INTO users (username, name, password, email, phone_number) VALUES
    (
    'username_1', 
    'name_1', 
    'scrypt:32768:8:1$n952oFWoS88c2UCd$b030f2524c51d45b866f128a92335d05d3be6ec27c0c153d4db9e58514ffbab4f4bea39d93694cfd5ae4eb2d51f6a10b866ae87057a7cd246f4eadf37576308d', 
    'email_1@gmail.com',
    '07777111111'),
    ('username_2', 
    'name_2', 
    'scrypt:32768:8:1$lj6tuvqbfBTNIcMx$e8b2b2fe230d39e1f2afc1b07efcf578ee3a5fca9d0fe86d54f0ed8a7fb8118e1330edccac8d317069ed944a4d55f8ca56a14bcf13734d43aae9eff172080dc1', 
    'email_2@gmail.com', 
    '07777222222'),
    ('username_3',
    'name_3', 
    'scrypt:32768:8:1$4gQwh0IBZhJT1zfR$c982b4bb7302984ec2d00c94543f6f76c4d7fd1dbdbb54a1a3c80e7950dd123c73243f1e9f61df48d0462840ed3991b32b0d5580d2cd117baf1d7575fda5887e', 
    'email_3@gmail.com', 
    '07777333333'),
    ('username_4', 
    'name_4', 
    'scrypt:32768:8:1$9pYICBsdVAMXmYDf$84874786e7328395fa9ca8a351cbb8e9f188a11ef848da1c481a087c9d10309235e8f8383ab9dad868158f4469f49c59ba527db89e55e1b960bbe4f7d8fd6489', 
    'email_4@gmail.com', 
    '07777444444'),
    ('username_5', 
    'name_5', 
    'scrypt:32768:8:1$zhxGDR4mT5ugZpvg$7de034a2737b35b5dd32a088d2cd3cdeea9d25a509fc63948bf59a406c94a50c4f014b7a38b88d54f98c4fa2d730568f3246b093e34ec4963dc9f4ba6dc4807e', 
    'email_5@gmail.com', 
    '07777555555'),
    ('username_6', 
    'name_6', 
    'scrypt:32768:8:1$r7vZLTA3ZRRW97YS$a2622f89ef8f56ca06242aa159e167669d944e73ac46a1f0e433c277e3ff190a78f9922fb49c9dc802d2f0bf2ecbbcd4ebfd2803faa4272799e2167935050999', 
    'email_6@gmail.com', 
    '07777666666'),
    ('username_7', 
    'name_7', 
    'scrypt:32768:8:1$WIy64XSygROIdADx$f87b6126d04425746dd369cda17dfd3c1a08ca97a0dff5f04afb60bc03f6fb27f602460aa4fbb3f177f8559414d31577fbd506466f5620a94678cdf206f54c34', 
    'email_7@gmail.com', 
    '07777777777'),
    ('username_8', 
    'name_8', 
    'scrypt:32768:8:1$Ts4bSD4dlXBUbhIf$daf77c6ac4326fb35fa73fe75a031bfa44a9050639c665a974bc81d4bb62f1a48aab87626b75d73c128a2215b037bc19152c1f8d482d0ad7f62cbb2bd18a759b', 
    'email_8@gmail.com', 
    '07777888888');

INSERT INTO spaces (name, address, description, price, dates_booked, owner_id) VALUES
    ('Stratfest','Wembley','Company event space',1000.50,'[2024-09-14, 2024-09-15, 2024-09-16]', 1), -- Owned by User 1
    ('Big House','11 Example Street','Vibrant neighbourhood',200,'[2024-10-14, 2024-10-15, 2024-10-16, 2024-10-17]', 1), -- Owned by User 1
    ('Big Hotel','4 Street','Dangerous area',150.99,'[]', 2), -- Owned by User 2
    ('Small House','5 street','Peterborough',00.00,'[]', 3), -- Owned by User 3
    ('Conference Center', '99 Main St', 'Large event venue', 1500.75, '[2024-09-20, 2024-09-21, 2024-09-22]', 1), -- Owned by User 1
    ('Art Gallery', '1 Art St', 'Modern and spacious', 500.00, '[2024-10-01, 2024-10-02]', 5), -- Owned by User 5
    ('Beach House', '10 Beach Ave', 'Seaside retreat', 300.00, '[2024-11-10, 2024-11-15]', 6), -- Owned by User 6
    ('Cabin in Woods', 'Forest Road', 'Rustic cabin in forest', 125.00, '[2024-12-01, 2024-12-05]', 7), -- Owned by User 7
    ('City Apartment', '100 Urban St', 'Cozy city apartment', 120.00, '[2024-12-15, 2024-12-20]', 8), -- Owned by User 8
    ('Penthouse Suite', '50 Lux Ave', 'Luxury penthouse', 2500.00, '[]', 5), -- Owned by User 5
    ('Lake House', '22 Lake View', 'Quiet lakefront house', 350.00, '[2024-12-05, 2024-12-10]', 7), -- Owned by User 7
    ('Farmhouse', '9 Country Rd', 'Countryside farmhouse', 80.00, '[2024-12-25, 2024-12-30]', 6); -- Owned by User 6

INSERT INTO bookings (check_in, check_out, user_id, space_id, owner_id, approved) VALUES
    ('2024-12-01', '2024-12-07', 1, 1, 1, TRUE),           -- User 1 booking Space 1 owned by User 1
    ('2024-12-07', '2024-12-12', 2, 1, 1, TRUE),           -- User 2 booking Space 1 owned by User 1
    ('2024-12-16', '2024-12-20', 1, 1, 1, FALSE),          -- User 1 booking Space 1 owned by User 1
    ('2024-12-22', '2024-12-23', 2, 1, 1, TRUE),           -- User 2 booking Space 1 owned by User 1
    ('2024-12-26', '2025-01-01', 1, 1, 1, FALSE),          -- User 1 booking Space 1 owned by User 1
    ('2024-12-26', '2025-01-01', 2, 2, 1, TRUE),           -- User 2 booking Space 2 owned by User 1
    ('2024-12-01', '2024-12-03', 4, 1, 1, TRUE),           -- User 4 booking Space 1 owned by User 1
    ('2024-12-08', '2024-12-15', 5, 2, 1, FALSE),          -- User 5 booking Space 2 owned by User 1
    ('2024-12-16', '2024-12-20', 6, 3, 2, TRUE),           -- User 6 booking Space 3 owned by User 2
    ('2024-12-20', '2024-12-25', 3, 4, 3, TRUE),           -- User 3 booking Space 4 owned by User 3
    ('2024-12-10', '2024-12-12', 7, 4, 3, FALSE),          -- User 7 booking Space 4 owned by User 3
    ('2024-12-15', '2024-12-18', 8, 5, 1, TRUE),           -- User 8 booking Space 5 owned by User 1
    ('2024-11-05', '2024-11-10', 4, 6, 5, TRUE),           -- User 4 booking Space 6 owned by User 5
    ('2024-12-01', '2024-12-05', 5, 7, 6, TRUE),           -- User 5 booking Space 7 owned by User 6
    ('2024-12-06', '2024-12-09', 6, 8, 7, FALSE),          -- User 6 booking Space 8 owned by User 7
    ('2024-12-20', '2024-12-27', 3, 9, 8, TRUE),           -- User 3 booking Space 9 owned by User 8
    ('2024-12-28', '2025-01-02', 7, 2, 1, TRUE),           -- User 7 booking Space 2 owned by User 1
    ('2025-01-05', '2025-01-10', 4, 3, 2, FALSE);          -- User 4 booking Space 3 owned by User 2
