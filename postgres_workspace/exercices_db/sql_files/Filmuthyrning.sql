CREATE DATABASE movie_rental;

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    membership_level VARCHAR(20) DEFAULT 'basic',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    director VARCHAR(100),
    release_year INTEGER,
    rating DECIMAL(3,1) CHECK (rating >= 1 AND rating <= 10),
    available_copies INTEGER DEFAULT 0 CHECK (available_copies >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE rentals (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id) ON DELETE CASCADE,
    movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
    rental_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    cost DECIMAL(10,2) CHECK (cost > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customers (name, email, phone, membership_level) VALUES
('Anna Andersson', 'anna@email.com', '070-1234567', 'premium'),
('Erik Eriksson', 'erik@email.com', '070-2345678', 'basic');

INSERT INTO movies (title, director, release_year, rating, available_copies) VALUES
('The Matrix', 'Wachowski Sisters', 1999, 8.7, 3),
('Inception', 'Christopher Nolan', 2010, 8.8, 2),
('Interstellar', 'Christopher Nolan', 2014, 8.6, 1);

INSERT INTO rentals (customer_id, movie_id, rental_date, cost) VALUES
(1, 1, CURRENT_DATE, 49.00),
(2, 2, CURRENT_DATE - INTERVAL '2 days', 39.00);

SELECT * FROM customers;
SELECT * FROM movies;
SELECT * FROM rentals;