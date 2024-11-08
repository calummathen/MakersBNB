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
    'scrypt:32768:8:1$GfLBQKb43qaFVRrk$0a256abf07116c1f4bb96c551c25c8d8c2639d763fe74b464b0df5c6311ba534a11da91719514253e4abf5a7a00b78006b00010b95a931eefc56e1f8bec6680b', 
    'leadercalum1@gmail.com',
    '07777111111');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Cezary_KB13', 
    'Cezary_Karwoski-Budd', 
    'scrypt:32768:8:1$71Vgra5I4VOY0hdc$3144310326a12f8430919cacd1386a6c6922e9367a4be3b4eff524524e6107bcaa6c98c2df59b54824f4ff8966b86417e9c474fc28f687c2e39fbc2d9cb209e0',  
    'c_kb13@gmail.com', 
    '07777222222');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Jamie_Pod1',
    'Jamie_Plumb', 
    'scrypt:32768:8:1$IA28TTBBVXpDrZMx$2f93382aac7f4d83779c683ccfd19f44ad20e147fc912b1d14eb3dbd61d2d22afec2c3766af763ead3e5b069dd8707b314b47eb560c498bbbd0df3642b7f7b75',
    'Jpod1@email_3@gmail.com', 
    '07777333333');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Pat_Shannon',
    'Patrick Shannon', 
    'scrypt:32768:8:1$1Nzh2Ec3aLS6cxu3$e1aec54c3aecd08dc344b248fb875de17d63f337dbaeb25baf0f92c60424cab00573c86af3552440c8070e554d5b44676ce22ce35880dd9ba6f5278357854c00', 
    'patshannon2@outlook.com', 
    '07777444444');
INSERT INTO users (username, name, password, email, phone_number) VALUES(
    'Shaker_H',
    'Shaker Hussain', 
    'scrypt:32768:8:1$fIb9bnpnyOScBhVL$1ddeb901bb103ea42a8fa386322eb7b88b8b421814dd8597add30e4266cb0053a14a0162953ba4e7bee2a5801be2524ea154c6a6cf7e4d70cde52d11398afec6', 
    'shaker_h@gmail.com', 
    '07777555555');




INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Seaside Cottage', '1 Ocean Road, Cornwall', 'A cozy cottage overlooking the Cornish coast.', 150.00, '["2024-12-20", "2024-12-21"]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Highland Retreat', '23 Glen Road, Fort William', 'Remote cabin with breathtaking views of the Highlands.', 220.00, '["2025-01-10", "2025-01-15"]', 2);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Central London Flat', '45 Baker Street, London', 'Stylish flat in the heart of the city, close to attractions.', 450.00, '[]', 3);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('York Minster View Apartment', '14 Minster Yard, York', 'Beautiful apartment with views of York Minster.', 170.00, '[]', 4);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Lake District Cabin', '8 Windermere Lane, Cumbria', 'Rustic cabin near Lake Windermere.', 200.00, '["2024-11-23", "2024-11-27"]', 5);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Brighton Beach House', '56 Seafront Road, Brighton', 'Modern house near the beach.', 160.00, '[]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Scottish Castle Suite', 'Castle Drive, Edinburgh', 'Luxury suite within a historic Scottish castle.', 350.00, '["2024-12-30", "2025-01-02"]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Oxford Countryside Bungalow', '3 Meadows End, Oxford', 'Peaceful bungalow in the countryside', 140.00, '[]', 2);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Historic Bath Apartment', '22 Roman Street, Bath', 'Charming apartment near the Roman Baths.', 210.00, '[]', 2);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Norfolk Seaside Escape', '7 Pier View, Cromer', 'Quaint seaside home with easy beach access.', 140.00, '[]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Bristol City Loft', '9 Harbourside, Bristol', 'Loft with panoramic city views.', 175.00, '[]', 1);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Charming Cotswolds Cottage', '2 Market Square, Chipping Campden', 'Traditional cottage in the picturesque Cotswolds.', 155.00, '["2025-02-14", "2025-02-16"]', 4);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Liverpool Dock Apartment', '41 Dockside Lane, Liverpool', 'Modern apartment with views of the historic docks.', 160.00, '[]', 4);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Cambridge River View', '15 Riverside Walk, Cambridge', 'Elegant apartment along the River Cam.', 185.00, '["2025-03-05", "2025-03-07"]', 3);
INSERT INTO spaces(name,address,description,price,dates_booked,owner_id) VALUES('Adventure Cottage', '6 Mountain Lane, Snowdonia', 'Cottage with incredible views.', 165.00, '["2025-01-01", "2025-01-03"]', 5);

