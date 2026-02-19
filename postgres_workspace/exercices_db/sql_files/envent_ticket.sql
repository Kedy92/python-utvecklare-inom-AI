CREATE DATABASE event_tickets;

CREATE TABLE venues (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    address VARCHAR(200),
    city VARCHAR(100),
    capacity INTEGER CHECK (capacity > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    venue_id INTEGER REFERENCES venues(id) ON DELETE CASCADE,
    event_date TIMESTAMP NOT NULL,
    event_type VARCHAR(50),
    ticket_price DECIMAL(10,2) CHECK (ticket_price > 0),
    tickets_available INTEGER CHECK (tickets_available >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id) ON DELETE CASCADE,
    event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    num_tickets INTEGER CHECK (num_tickets > 0),
    total_cost DECIMAL(10,2) CHECK (total_cost > 0),
    payment_status VARCHAR(20) DEFAULT 'pending' CHECK (payment_status IN ('pending', 'paid', 'cancelled')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Testdata
INSERT INTO venues (name, address, city, capacity) VALUES
('Globen', 'Globentorget 2', 'Stockholm', 16000),
('Ullevi', 'Ullevigatan', 'Göteborg', 43000),
('Malmö Arena', 'Hyllie Stationstorg 2', 'Malmö', 15500);

INSERT INTO events (name, venue_id, event_date, event_type, ticket_price, tickets_available) VALUES
('Coldplay Concert', 1, '2024-12-15 19:00:00', 'Concert', 899.00, 15000),
('Fotbollsmatch: Sverige vs Norge', 2, '2024-11-20 18:00:00', 'Sports', 350.00, 40000),
('Melodifestivalen', 3, '2025-02-14 20:00:00', 'Concert', 599.00, 14000);

INSERT INTO customers (name, email, phone) VALUES
('Anna Andersson', 'anna@email.com', '070-1234567'),
('Erik Eriksson', 'erik@email.com', '070-2345678'),
('Maria Svensson', 'maria@email.com', '070-3456789');

INSERT INTO bookings (customer_id, event_id, num_tickets, total_cost, payment_status) VALUES
(1, 1, 2, 1798.00, 'paid'),
(2, 2, 4, 1400.00, 'paid'),
(3, 1, 1, 899.00, 'pending');

-- Verifiera
SELECT * FROM venues;
SELECT * FROM events;
SELECT * FROM customers;
SELECT * FROM bookings;

-- Bonus: För att säkerställa tillgänglighet skulle man behöva en trigger
-- eller hantera detta i applikationslogiken
