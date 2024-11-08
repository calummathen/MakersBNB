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
    'Leader_Calum', 
    'Calum_Mathen', 
    'scrypt:32768:8:1$n952oFWoS88c2UCd$b030f2524c51d45b866f128a92335d05d3be6ec27c0c153d4db9e58514ffbab4f4bea39d93694cfd5ae4eb2d51f6a10b866ae87057a7cd246f4eadf37576308d', 
    'leadercalum1@gmail.com',
    '07777111111');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Cezary_KB13', 
    'Cezary_Karwoski-Budd', 
    'scrypt:32768:8:1$lj6tuvqbfBTNIcMx$e8b2b2fe230d39e1f2afc1b07efcf578ee3a5fca9d0fe86d54f0ed8a7fb8118e1330edccac8d317069ed944a4d55f8ca56a14bcf13734d43aae9eff172080dc1', 
    'c_kb13@gmail.com', 
    '07777222222');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Jamie_Pod1',
    'Jamie_Plumb', 
    'scrypt:32768:8:1$4gQwh0IBZhJT1zfR$c982b4bb7302984ec2d00c94543f6f76c4d7fd1dbdbb54a1a3c80e7950dd123c73243f1e9f61df48d0462840ed3991b32b0d5580d2cd117baf1d7575fda5887e', 
    'Jpod1@email_3@gmail.com', 
    '07777333333');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Pat_Shannon',
    'Patrick Shannon', 
    'scrypt:', 
    'patshannon2@outlook.com', 
    '07777444444');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Shaker_H',
    'Shaker Hussain', 
    'scrypt:', 
    'shaker_h@gmail.com', 
    '07777555555');




INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Seaside Cottage', '1 Ocean Road, Cornwall', 'A cozy cottage overlooking the Cornish coast.', 150.00, '["2024-12-20", "2024-12-21"]', 1),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Highland Retreat', '23 Glen Road, Fort William', 'Remote cabin with breathtaking views of the Highlands.', 220.00, '["2025-01-10", "2025-01-15"]', 2),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Central London Flat', '45 Baker Street, London', 'Stylish flat in the heart of the city, close to attractions.', 450.00, '[]', 3),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('York Minster View Apartment', '14 Minster Yard, York', 'Beautiful apartment with views of York Minster.', 170.00, '[]', 4),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Lake District Cabin', '8 Windermere Lane, Cumbria', 'Rustic cabin near Lake Windermere.', 200.00, '["2024-11-23", "2024-11-27"]', 5),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Brighton Beach House', '56 Seafront Road, Brighton', 'Modern house near the beach.', 160.00, '[]', 1),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Scottish Castle Suite', 'Castle Drive, Edinburgh', 'Luxury suite within a historic Scottish castle.', 350.00, '["2024-12-30", "2025-01-02"]', 1),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Oxford Countryside Bungalow', '3 Meadows End, Oxford', 'Peaceful bungalow in the countryside', 140.00, '[]', 2),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Historic Bath Apartment', '22 Roman Street, Bath', 'Charming apartment near the Roman Baths.', 210.00, '[]', 2),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Norfolk Seaside Escape', '7 Pier View, Cromer', 'Quaint seaside home with easy beach access.', 140.00, '[]', 1),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Bristol City Loft', '9 Harbourside, Bristol', 'Loft with panoramic city views.', 175.00, '[]', 11),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Charming Cotswolds Cottage', '2 Market Square, Chipping Campden', 'Traditional cottage in the picturesque Cotswolds.', 155.00, '["2025-02-14", "2025-02-16"]', 4),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Liverpool Dock Apartment', '41 Dockside Lane, Liverpool', 'Modern apartment with views of the historic docks.', 160.00, '[]', 4),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Cambridge River View', '15 Riverside Walk, Cambridge', 'Elegant apartment along the River Cam.', 185.00, '["2025-03-05", "2025-03-07"]', 3),
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Adventure Cottage', '6 Mountain Lane, Snowdonia', 'Cottage with incredible views.', 165.00, '["2025-01-01", "2025-01-03"]', 5);

