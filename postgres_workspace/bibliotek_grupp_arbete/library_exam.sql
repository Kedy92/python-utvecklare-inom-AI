-- Skapa databas om den inte finns
CREATE DATABASE library_db;


-- Ta bort befintliga tabeller om de finns (i rätt ordning p.g.a. foreign keys)
DROP TABLE IF EXISTS loans CASCADE;
DROP TABLE IF EXISTS members CASCADE;
DROP TABLE IF EXISTS books CASCADE;

-- Skapa Books tabell
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    publication_year INTEGER,
    category VARCHAR(100),
    total_copies INTEGER DEFAULT 1 CHECK (total_copies >= 0),
    available_copies INTEGER DEFAULT 1 CHECK (available_copies >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_available_not_exceed_total CHECK (available_copies <= total_copies)
);

-- Skapa Members tabell
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    membership_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Skapa Loans tabell
CREATE TABLE loans (
    id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    member_id INTEGER NOT NULL,
    loan_date DATE DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE RESTRICT,
    CONSTRAINT fk_member FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE,
    CONSTRAINT check_due_after_loan CHECK (due_date > loan_date),
    CONSTRAINT check_return_after_loan CHECK (return_date IS NULL OR return_date >= loan_date)
);

-- Skapa index för bättre prestanda
CREATE INDEX idx_books_title ON books(title);
CREATE INDEX idx_books_author ON books(author);
CREATE INDEX idx_books_category ON books(category);
CREATE INDEX idx_books_isbn ON books(isbn);

CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_members_last_name ON members(last_name);

CREATE INDEX idx_loans_book_id ON loans(book_id);
CREATE INDEX idx_loans_member_id ON loans(member_id);
CREATE INDEX idx_loans_loan_date ON loans(loan_date);
CREATE INDEX idx_loans_due_date ON loans(due_date);
CREATE INDEX idx_loans_return_date ON loans(return_date);



-- ===========================
-- Testdata för books
-- ===========================
INSERT INTO books (title, author, isbn, publication_year, category, total_copies, available_copies)
VALUES 
('1984', 'George Orwell', '9780451524935', 1949, 'Dystopian', 5, 3),
('To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960, 'Fiction', 4, 2),
('The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 'Classic', 3, 1),
('Pride and Prejudice', 'Jane Austen', '9780141439518', 1813, 'Romance', 4, 4),
('The Catcher in the Rye', 'J.D. Salinger', '9780316769488', 1951, 'Fiction', 6, 5),
('The Hobbit', 'J.R.R. Tolkien', '9780547928227', 1937, 'Fantasy', 7, 7),
('Fahrenheit 451', 'Ray Bradbury', '9781451673319', 1953, 'Dystopian', 3, 0),
('Brave New World', 'Aldous Huxley', '9780060850524', 1932, 'Dystopian', 2, 2),
('Moby Dick', 'Herman Melville', '9781503280786', 1851, 'Adventure', 2, 1),
('War and Peace', 'Leo Tolstoy', '9781400079988', 1869, 'Historical', 3, 3),
('The Lord of the Rings', 'J.R.R. Tolkien', '9780544003415', 1954, 'Fantasy', 5, 2),
('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', '9780590353427', 1997, 'Fantasy', 6, 4),
('The Alchemist', 'Paulo Coelho', '9780061122415', 1988, 'Adventure', 3, 2),
('The Da Vinci Code', 'Dan Brown', '9780307474278', 2003, 'Mystery', 4, 1),
('The Girl with the Dragon Tattoo', 'Stieg Larsson', '9780307454546', 2005, 'Mystery', 5, 5);

-- ===========================
-- Testdata för members
-- ===========================
INSERT INTO members (first_name, last_name, email, phone, membership_date)
VALUES
('Anna', 'Svensson', 'anna.svensson@email.com', '0701234567', '2023-02-10'),
('Erik', 'Johansson', 'erik.johansson@email.com', '0702345678', '2024-01-15'),
('Maria', 'Andersson', 'maria.andersson@email.com', '0703456789', '2024-03-22'),
('Johan', 'Karlsson', 'johan.karlsson@email.com', '0704567890', '2023-11-05'),
('Sara', 'Nilsson', 'sara.nilsson@email.com', '0705678901', '2024-06-17'),
('Lars', 'Olsson', 'lars.olsson@email.com', '0706789012', '2023-12-25'),
('Emma', 'Berg', 'emma.berg@email.com', '0707890123', '2024-07-08'),
('Fredrik', 'Lind', 'fredrik.lind@email.com', '0708901234', '2024-09-14'),
('Karin', 'Hansson', 'karin.hansson@email.com', '0709012345', '2023-10-30'),
('Peter', 'Gustafsson', 'peter.gustafsson@email.com', '0700123456', '2024-02-05');

-- ===========================
-- Testdata för loans
-- ===========================
-- Aktiva lån (return_date = NULL)
INSERT INTO loans (book_id, member_id, due_date)
VALUES
(1, 1, CURRENT_DATE + INTERVAL '14 days'),
(2, 2, CURRENT_DATE + INTERVAL '7 days'),
(3, 3, CURRENT_DATE + INTERVAL '21 days'),
(4, 4, CURRENT_DATE + INTERVAL '10 days'),
(5, 5, CURRENT_DATE + INTERVAL '14 days'),
(6, 6, CURRENT_DATE + INTERVAL '30 days'),
(7, 7, CURRENT_DATE + INTERVAL '5 days');



INSERT INTO loans (book_id, member_id, loan_date, due_date, return_date)
VALUES
-- 1️ Active loan (not returned yet)
(3, 1, CURRENT_DATE - INTERVAL '5 days', CURRENT_DATE + INTERVAL '10 days', NULL),

-- 2️ Active loan (still within due_date)
(7, 2, CURRENT_DATE - INTERVAL '2 days', CURRENT_DATE + INTERVAL '3 days', NULL),

-- 3️ Returned loan (returned early)
(4, 5, CURRENT_DATE - INTERVAL '12 days', CURRENT_DATE - INTERVAL '2 days', CURRENT_DATE - INTERVAL '3 days'),

-- 4️ Returned on time
(9, 3, CURRENT_DATE - INTERVAL '20 days', CURRENT_DATE - INTERVAL '10 days', CURRENT_DATE - INTERVAL '9 days'),

-- 5️ Returned late (overdue return)
(6, 6, CURRENT_DATE - INTERVAL '30 days', CURRENT_DATE - INTERVAL '20 days', CURRENT_DATE - INTERVAL '5 days'),

-- 6️ Overdue (due date passed, return_date still NULL)
(10, 4, CURRENT_DATE - INTERVAL '15 days', CURRENT_DATE - INTERVAL '3 days', NULL),

-- 7️ Another overdue loan
(2, 8, CURRENT_DATE - INTERVAL '18 days', CURRENT_DATE - INTERVAL '1 day', NULL);



-- Återlämnade lån (return_date satt) ----Få kolla sen(ingår inte)
INSERT INTO loans (book_id, member_id, due_date, return_date)
VALUES
(8, 8, CURRENT_DATE - INTERVAL '20 days', CURRENT_DATE - INTERVAL '10 days'),
(9, 9, CURRENT_DATE - INTERVAL '15 days', CURRENT_DATE - INTERVAL '5 days'),
(10, 10, CURRENT_DATE - INTERVAL '30 days', CURRENT_DATE - INTERVAL '2 days'),
(11, 1, CURRENT_DATE - INTERVAL '25 days', CURRENT_DATE - INTERVAL '20 days'),
(12, 2, CURRENT_DATE - INTERVAL '10 days', CURRENT_DATE - INTERVAL '5 days'),
(13, 3, CURRENT_DATE - INTERVAL '7 days', CURRENT_DATE - INTERVAL '3 days'),
(14, 4, CURRENT_DATE - INTERVAL '12 days', CURRENT_DATE - INTERVAL '6 days');

-- Försenade lån (due_date har passerat men return_date är NULL) -- ska kollas sen
INSERT INTO loans (book_id, member_id, due_date)
VALUES
(15, 5, CURRENT_DATE - INTERVAL '3 days'),
(1, 6, CURRENT_DATE - INTERVAL '1 days'),
(2, 7, CURRENT_DATE - INTERVAL '2 days');


-- Försenade lån (due_date har passerat men return_date är NULL)
INSERT INTO loans (book_id, member_id, loan_date, due_date)
VALUES
(15, 5, CURRENT_DATE - INTERVAL '10 days', CURRENT_DATE - INTERVAL '3 days'),
(1, 6, CURRENT_DATE - INTERVAL '12 days', CURRENT_DATE - INTERVAL '1 days'),
(2, 7, CURRENT_DATE - INTERVAL '8 days', CURRENT_DATE - INTERVAL '2 days');




-- ============================================
-- SQL QUERIES FÖR LIBRARY MANAGEMENT SYSTEM
-- ============================================
-- Detta dokument innehåller 15+ queries som demonstrerar:
-- - Grundläggande SQL (SELECT, WHERE, ORDER BY)
-- - JOIN-operationer (INNER JOIN, LEFT JOIN)
-- - Aggregeringsfunktioner (COUNT, SUM, AVG, MIN, MAX)
-- - Gruppering (GROUP BY, HAVING)
-- - Subqueries och avancerade tekniker
-- ============================================

-- ============================================
-- GRUNDLÄGGANDE QUERIES (5 st)
-- ============================================

-- QUERY 1: Hämta alla böcker sorterade efter titel
-- Syfte: Visa alla böcker i alfabetisk ordning
-- Tekniker: SELECT, ORDER BY
SELECT 
    id,
    title,
    author,
    category,
    publication_year,
    available_copies,
    total_copies
FROM books
ORDER BY title ASC;

-- Förväntat resultat: Alla böcker alfabetiskt, t.ex. "1984" först


-- QUERY 2: Hämta alla medlemmar som blev medlemmar under 2024
-- Syfte: Hitta nya medlemmar från innevarande år
-- Tekniker: SELECT, WHERE, EXTRACT, ORDER BY
SELECT 
    id,
    first_name,
    last_name,
    email,
    phone,
    membership_date
FROM members
WHERE EXTRACT(YEAR FROM membership_date) = 2024
ORDER BY membership_date DESC;

-- Förväntat resultat: 8+ medlemmar som registrerades 2024


-- QUERY 3: Hämta alla böcker i kategorin "Fiction"
-- Syfte: Filtrera böcker efter genre
-- Tekniker: SELECT, WHERE, ORDER BY
SELECT 
    id,
    title,
    author,
    publication_year,
    available_copies,
    total_copies
FROM books
WHERE category = 'Fiction'
ORDER BY title;

-- Förväntat resultat: Böcker som "1984", "Pride and Prejudice", etc.


-- QUERY 4: Hämta alla aktiva lån (inte återlämnade)
-- Syfte: Se vilka böcker som är utlånade just nu
-- Tekniker: SELECT, WHERE IS NULL, ORDER BY
SELECT 
    id,
    book_id,
    member_id,
    loan_date,
    due_date,
    CURRENT_DATE - due_date AS days_until_due
FROM loans
WHERE return_date IS NULL
ORDER BY due_date ASC;

-- Förväntat resultat: Lån utan return_date, sorterade efter förfallodatum


-- QUERY 5: Hämta böcker med ISBN-nummer
-- Syfte: Visa böcker som har registrerat ISBN
-- Tekniker: SELECT, WHERE IS NOT NULL, ORDER BY
SELECT 
    id,
    title,
    author,
    isbn,
    publication_year,
    category
FROM books
WHERE isbn IS NOT NULL
ORDER BY title;

-- Förväntat resultat: Alla böcker som har ISBN registrerat


-- ============================================
-- JOIN-QUERIES (5 st)
-- ============================================

-- QUERY 6: Visa alla lån med bokens titel och medlemmens namn
-- Syfte: Komplett låneinformation från tre tabeller
-- Tekniker: INNER JOIN (2 joins), CONCAT, CASE
SELECT 
    l.id AS loan_id,
    b.title AS book_title,
    b.author AS book_author,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.email AS member_email,
    l.loan_date,
    l.due_date,
    l.return_date,
    CASE 
        WHEN l.return_date IS NULL AND l.due_date < CURRENT_DATE THEN 'Overdue'
        WHEN l.return_date IS NULL THEN 'Active'
        ELSE 'Returned'
    END AS status
FROM loans l
INNER JOIN books b ON l.book_id = b.id
INNER JOIN members m ON l.member_id = m.id
ORDER BY l.loan_date DESC;

-- Förväntat resultat: Alla lån med bok och medlemsinformation


-- QUERY 7: Visa alla böcker en specifik medlem har lånat
-- Syfte: Lånehistorik för en medlem
-- Tekniker: INNER JOIN, WHERE, ORDER BY
SELECT 
    b.id AS book_id,
    b.title,
    b.author,
    b.category,
    l.loan_date,
    l.due_date,
    l.return_date,
    CASE 
        WHEN l.return_date IS NULL THEN 'Currently borrowed'
        WHEN l.return_date > l.due_date THEN 'Returned late'
        ELSE 'Returned on time'
    END AS status
FROM loans l
INNER JOIN books b ON l.book_id = b.id
WHERE l.member_id = 1  -- Anna Andersson
ORDER BY l.loan_date DESC;

-- Förväntat resultat: Alla böcker som medlem #1 har lånat


-- QUERY 8: Visa alla medlemmar som har lånat böcker av en specifik författare
-- Syfte: Hitta läsare av en viss författare
-- Tekniker: INNER JOIN (multiple), WHERE, DISTINCT
SELECT DISTINCT
    m.id,
    m.first_name,
    m.last_name,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.email,
    b.author
FROM members m
INNER JOIN loans l ON m.id = l.member_id
INNER JOIN books b ON l.book_id = b.id
WHERE b.author = 'George Orwell'
ORDER BY m.last_name, m.first_name;



-- Förväntat resultat: Medlemmar som lånat böcker av George Orwell


-- QUERY 9: Visa böcker som aldrig har lånats
-- Syfte: Identifiera opopulära böcker
-- Tekniker: LEFT JOIN, WHERE IS NULL
SELECT 
    b.id,
    b.title,
    b.author,
    b.category,
    b.publication_year,
    b.total_copies
FROM books b
LEFT JOIN loans l ON b.id = l.book_id
WHERE l.id IS NULL
ORDER BY b.title;

-- Förväntat resultat: Böcker utan någon lån-post


-- QUERY 10: Visa medlemmar som inte har några aktiva lån
-- Syfte: Hitta medlemmar som kan uppmuntras att låna
-- Tekniker: LEFT JOIN, WHERE IS NULL, subquery condition
SELECT 
    m.id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.email,
    m.membership_date,
    CURRENT_DATE - m.membership_date AS days_member
FROM members m
LEFT JOIN loans l ON m.id = l.member_id AND l.return_date IS NULL
WHERE l.id IS NULL
ORDER BY m.membership_date DESC;

-- Förväntat resultat: Medlemmar utan aktiva lån just nu


-- ============================================
-- AGGREGERING OCH ANALYS (5 st)
-- ============================================

-- QUERY 11: Räkna antal böcker per kategori
-- Syfte: Översikt av boksamlingens sammansättning
-- Tekniker: COUNT, SUM, GROUP BY, ORDER BY
SELECT 
    COALESCE(category, 'Uncategorized') AS category,
    COUNT(*) AS number_of_books,
    SUM(total_copies) AS total_copies,
    SUM(available_copies) AS available_copies,
    SUM(total_copies) - SUM(available_copies) AS borrowed_copies,
    ROUND(AVG(publication_year), 0) AS avg_publication_year
FROM books
GROUP BY category
ORDER BY number_of_books DESC, category;

-- Förväntat resultat: Kategorier med antal böcker och kopior


-- QUERY 12: Hitta de 5 mest populära böckerna (mest lånade)
-- Syfte: Identifiera populära böcker för inköp av fler exemplar
-- Tekniker: INNER JOIN, COUNT, GROUP BY, ORDER BY, LIMIT
SELECT 
    b.id,
    b.title,
    b.author,
    b.category,
    COUNT(l.id) AS times_borrowed,
    b.total_copies,
    ROUND(COUNT(l.id)::NUMERIC / b.total_copies, 2) AS loans_per_copy
FROM books b
INNER JOIN loans l ON b.id = l.book_id
GROUP BY b.id, b.title, b.author, b.category, b.total_copies
ORDER BY times_borrowed DESC, b.title
LIMIT 5;

-- Förväntat resultat: Top 5 mest lånade böcker


-- QUERY 13: Visa medlemmar med flest antal lån
-- Syfte: Identifiera de mest aktiva läsarna
-- Tekniker: LEFT JOIN, COUNT, CASE, GROUP BY, ORDER BY
SELECT 
    m.id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.email,
    COUNT(l.id) AS total_loans,
    COUNT(CASE WHEN l.return_date IS NULL THEN 1 END) AS active_loans,
    COUNT(CASE WHEN l.return_date IS NOT NULL THEN 1 END) AS returned_loans,
    COUNT(CASE WHEN l.return_date IS NULL AND l.due_date < CURRENT_DATE THEN 1 END) AS overdue_loans
FROM members m
LEFT JOIN loans l ON m.id = l.member_id
GROUP BY m.id, m.first_name, m.last_name, m.email
HAVING COUNT(l.id) > 0
ORDER BY total_loans DESC, member_name;

-- Förväntat resultat: Medlemmar sorterade efter antal lån


-- QUERY 14: Beräkna genomsnittligt antal dagar mellan lånedatum och återlämning
-- Syfte: Analysera låneperioder
-- Tekniker: AVG, MIN, MAX, DATE arithmetic, WHERE IS NOT NULL
SELECT 
    COUNT(*) AS returned_books,
    ROUND(AVG(return_date - loan_date), 2) AS avg_days_borrowed,
    MIN(return_date - loan_date) AS shortest_loan_days,
    MAX(return_date - loan_date) AS longest_loan_days,
    ROUND(AVG(due_date - loan_date), 2) AS avg_loan_period,
    COUNT(CASE WHEN return_date > due_date THEN 1 END) AS returned_late,
    ROUND(100.0 * COUNT(CASE WHEN return_date > due_date THEN 1 END) / COUNT(*), 2) AS late_return_percentage
FROM loans
WHERE return_date IS NOT NULL;

-- Förväntat resultat: Statistik om låneperioder


-- QUERY 15: Visa hur många böcker som är försenade
-- Syfte: Identifiera försenade lån för uppföljning
-- Tekniker: COUNT, WHERE with multiple conditions, DISTINCT
SELECT 
    COUNT(*) AS overdue_loans,
    COUNT(DISTINCT book_id) AS overdue_books,
    COUNT(DISTINCT member_id) AS members_with_overdue,
    SUM(CURRENT_DATE - due_date) AS total_overdue_days,
    ROUND(AVG(CURRENT_DATE - due_date), 2) AS avg_days_overdue,
    MAX(CURRENT_DATE - due_date) AS most_overdue_days
FROM loans
WHERE return_date IS NULL 
    AND due_date < CURRENT_DATE;

-- Förväntat resultat: Antal och statistik för försenade lån


-- ============================================
-- BONUS QUERIES (Extra analys) - 3 st
-- ============================================

-- QUERY 16: Detaljerad lista över försenade lån med medlemsinfo
-- Syfte: Lista för uppföljning av försenade lån
-- Tekniker: INNER JOIN (multiple), WHERE, ORDER BY, DATE arithmetic
SELECT 
    l.id AS loan_id,
    b.title AS book_title,
    b.author,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.email,
    m.phone,
    l.loan_date,
    l.due_date,
    CURRENT_DATE - l.due_date AS days_overdue,
    CASE 
        WHEN CURRENT_DATE - l.due_date <= 7 THEN 'Reminder'
        WHEN CURRENT_DATE - l.due_date <= 14 THEN 'Warning'
        ELSE 'Urgent'
    END AS priority
FROM loans l
INNER JOIN books b ON l.book_id = b.id
INNER JOIN members m ON l.member_id = m.id
WHERE l.return_date IS NULL 
    AND l.due_date < CURRENT_DATE
ORDER BY days_overdue DESC, member_name;

-- Förväntat resultat: Detaljerad lista med kontaktinfo för uppföljning


-- QUERY 17: Komplett översikt av biblioteket (Dashboard)
-- Syfte: En query som ger översikt av hela systemet
-- Tekniker: Subqueries, aggregering
SELECT 
    (SELECT COUNT(*) FROM books) AS total_book_titles,
    (SELECT SUM(total_copies) FROM books) AS total_book_copies,
    (SELECT SUM(available_copies) FROM books) AS available_copies,
    (SELECT SUM(total_copies) - SUM(available_copies) FROM books) AS borrowed_copies,
    (SELECT COUNT(*) FROM members) AS total_members,
    (SELECT COUNT(*) FROM members WHERE membership_date >= CURRENT_DATE - INTERVAL '30 days') AS new_members_last_30_days,
    (SELECT COUNT(*) FROM loans) AS total_loans_all_time,
    (SELECT COUNT(*) FROM loans WHERE return_date IS NULL) AS active_loans,
    (SELECT COUNT(*) FROM loans WHERE return_date IS NOT NULL) AS returned_loans,
    (SELECT COUNT(*) FROM loans WHERE return_date IS NULL AND due_date < CURRENT_DATE) AS overdue_loans,
    (SELECT ROUND(AVG(return_date - loan_date), 2) FROM loans WHERE return_date IS NOT NULL) AS avg_loan_duration_days,
    (SELECT ROUND(100.0 * SUM(total_copies - available_copies) / SUM(total_copies), 2) FROM books) AS collection_utilization_percent;

-- Förväntat resultat: En rad med alla nyckeltal


-- QUERY 18: Mest aktiva lånare under senaste 30 dagarna
-- Syfte: Identifiera nyligen aktiva medlemmar
-- Tekniker: INNER JOIN, WHERE med datum, GROUP BY, HAVING, ORDER BY, LIMIT
SELECT 
    m.id,
    CONCAT(m.first_name, ' ', m.last_name) AS member_name,
    m.email,
    COUNT(l.id) AS loans_last_30_days,
    MIN(l.loan_date) AS first_loan_in_period,
    MAX(l.loan_date) AS last_loan_in_period,
    COUNT(CASE WHEN l.return_date IS NULL THEN 1 END) AS still_borrowed
FROM members m
INNER JOIN loans l ON m.id = l.member_id
WHERE l.loan_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY m.id, m.first_name, m.last_name, m.email
HAVING COUNT(l.id) > 0
ORDER BY loans_last_30_days DESC, member_name
LIMIT 10;

-- Förväntat resultat: Top 10 mest aktiva lånare senaste månaden


-- ============================================
-- SLUTKOMMENTAR
-- ============================================
-- Dessa 18 queries demonstrerar:
-- ✓ Grundläggande SQL (SELECT, WHERE, ORDER BY) - Query 1-5
-- ✓ JOIN-operationer (INNER, LEFT, DISTINCT) - Query 6-10
-- ✓ Aggregeringsfunktioner (COUNT, SUM, AVG, MIN, MAX) - Query 11-15
-- ✓ Gruppering och filtrering (GROUP BY, HAVING) - Query 11-15
-- ✓ Subqueries - Query 17
-- ✓ Datumberäkningar - Query 14, 16, 18
-- ✓ CASE-uttryck - Query 6, 7, 13, 14, 16
-- ✓ COALESCE för NULL-hantering - Query 11
-- ============================================