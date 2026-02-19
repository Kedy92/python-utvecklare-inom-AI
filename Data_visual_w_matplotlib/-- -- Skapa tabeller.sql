-- -- Skapa tabeller
-- CREATE TABLE students (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE,
--     grade VARCHAR(1) DEFAULT 'F',
--     department VARCHAR(50),
--     enrollment_year INTEGER,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE teachers (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE,
--     department VARCHAR(50),
--     hire_date DATE DEFAULT CURRENT_DATE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE courses (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     credits INTEGER DEFAULT 3,
--     teacher_id INTEGER REFERENCES teachers(id),
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );


-- CREATE TABLE enrollments (
--     id SERIAL PRIMARY KEY,
-- student_id INTEGER REFERENCES students(id),
-- course_id INTEGER REFERENCES cours(id),
-- enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- )

-- -- Constraints (begränsningar)
-- -- exempel:


-- CREATE TABLE products (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     price DECIMAL(10,2) CHECK (price>0),
--     stock INTEGER DEFAULT 0 CHECK (stock >= 0)
-- )

-- -- Dålig design (icke-normaliserad):

-- CREATE TABLE bad_enrollment(
--     id SERIAL PRIMARY KEY,
--     student_name VARCHAR(100),
--     student_emejl VARCHAR(100),
--     cours_name VARCHAR(100),
--     teacher_name VARCHAR(100)
-- )

-- CREATE TABLE students (id SERIAL PRIMARY KEY, name VARCHAR(100));
-- CREATE TABLE teachers (id SERIAL PRIMARY KEY, name VARCHAR(100));
-- CREATE TABLE cours (id SERIAL PRIMARY KEY, name VARCHAR(100), teacher_id INTEGER REFERENCES teachers(id));
-- CREATE TABLE enrollments (id SERIAL PRIMARY KEY, 
--     student_id INTEGER REFERENCES students(id),
--     course_id INTEGER REFERENCES courses(id)
--     );



-- -- Skapa tabell
-- CREATE TABLE students (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     email VARCHAR(100) UNIQUE,
--     grade VARCHAR(1) DEFAULT 'F',
--     department VARCHAR(50),
--     enrollment_year INTEGER,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- -- Lägg till testdata
-- INSERT INTO students (name, email, grade, department, enrollment_year) VALUES
-- ('Anna Andersson', 'anna@email.com', 'A', 'Datavetenskap', 2023),
-- ('Erik Eriksson', 'erik@email.com', 'B', 'Matematik', 2023);

-- INSERT INTO students (name email, grade, departement, enrollment_year) VALUES
-- ('Osman', 'osse@live.se', 'A', 'PUAI', 2025);

-- -- Hämta data
-- SELECT * FROM students;

-------------------------------------------------

CREATE TABLE guest (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE room (
    id SERIAL PRIMARY KEY,
    number INTEGER UNIQUE NOT NULL,
    guest_id INTEGER REFERENCES guest(id),
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    room_is INTEGER REFERENCES room(id),
    guest_id INTEGER REFERENCES guest(id)
);

INSERT INTO guest(name, phone, email) VALUES
('Ashur', '123', 'ashur@htomail.com'),
('Ashur3', '123', 'ashur4@htomail.com'),
('Ashur3', '123', 'ashur7@htomail.com');

SELECT * FROM guest;

SELECT 
    name,   
    enreollment,    
    case 
        WHEN enrollment_year >= 2023 THEN 'First year'
        WHEN enrollment_year >= 2022 THEN 'First year'
        WHEN enrollment_year >= 2021 THEN 'First year'
        ELSE 'Senior'
    END AS year_level
FROM students;