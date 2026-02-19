-- Skapa din databas
CREATE DATABASE bibliotek;

-- Skapa tabeller 
CREATE TABLE  members(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    phone VARCHAR(20),
    membership_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    auther VARCHAR(100) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    category VARCHAR(50),
    available BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE books 
RENAME COLUMN auther to author 

ALTER 

CREATE TABLE loans(
    id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES members(id) ON DELETE CASCADE,
    book_id INTEGER REFERENCES books(id) ON DELETE CASCADE,
    loan_date DATE DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Lägg till testdata

INSERT INTO members (name, email, phone) VALUES
('Anna Andersson', 'anna@email.com', '070-1234567'),
('Erik Eriksson', 'erik@email.com', '070-2345678');

INSERT INTO books (title, author, isbn, category) VALUES
('Clean Code', 'Robert C. Martin', '9780132350884', 'Programming'),
('The Pragmatic Programmer', 'Andrew Hunt', '9780135957059', 'Programming');

-- Testa databasen
SELECT * FROM members;
SELECT * FROM books;
