CREATE DATABASE gym_system;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    membership_type VARCHAR(20) CHECK (membership_type IN ('basic', 'standard', 'premium')),
    start_date DATE DEFAULT CURRENT_DATE,
    end_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    CHECK (end_date IS NULL OR end_date > start_date),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE trainers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    specialization VARCHAR(100),
    hourly_rate DECIMAL(10,2) CHECK (hourly_rate > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE training_sessions (
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
    trainer_id INTEGER REFERENCES trainers(id) ON DELETE SET NULL,
    session_date TIMESTAMP NOT NULL,
    duration_minutes INTEGER CHECK (duration_minutes > 0),
    session_type VARCHAR(50),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Testdata
INSERT INTO members (name, email, phone, membership_type, start_date, end_date) VALUES
('Anna Andersson', 'anna@email.com', '070-1234567', 'premium', '2024-01-01', '2024-12-31'),
('Erik Eriksson', 'erik@email.com', '070-2345678', 'basic', '2024-06-01', '2024-12-31'),
('Maria Svensson', 'maria@email.com', '070-3456789', 'standard', '2024-09-01', NULL);

INSERT INTO trainers (name, email, specialization, hourly_rate) VALUES
('Lars Larsson', 'lars@gym.com', 'Strength Training', 500.00),
('Karin Karlsson', 'karin@gym.com', 'Yoga', 450.00),
('Johan Johansson', 'johan@gym.com', 'Cardio', 400.00);

INSERT INTO training_sessions (member_id, trainer_id, session_date, duration_minutes, session_type, notes) VALUES
(1, 1, '2024-10-20 10:00:00', 60, 'Personal Training', 'Fokus på styrketräning'),
(1, 2, '2024-10-21 14:00:00', 45, 'Yoga', 'Nybörjarnivå'),
(2, 1, '2024-10-22 09:00:00', 60, 'Personal Training', 'Första passet'),
(3, 3, '2024-10-23 16:00:00', 30, 'Cardio', 'HIIT träning');

-- Verifiera
SELECT * FROM members;
SELECT * FROM trainers;
SELECT * FROM training_sessions;
