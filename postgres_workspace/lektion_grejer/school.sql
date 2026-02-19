-- Clean setup

CREATE DATABASE school;

-- 1️⃣ Students
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    grade VARCHAR(1) DEFAULT 'F',
    department VARCHAR(50),
    enrollment_year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students_backup (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    grade VARCHAR(1) DEFAULT 'F'
);

SELECT id, name FROM students ORDER BY id;

INSERT INTO enrollments (student_id, course_id, grade)
VALUES (9, 3, 'A');   -- Maria = id 9

-- 2️⃣ Teachers
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    department VARCHAR(100)
);

-- 3️⃣ Courses
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    credits INTEGER DEFAULT 3,
    teacher_id INTEGER REFERENCES teachers(id)
);

-- 4️⃣ Enrollments (Many-to-Many between students and courses)
CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(id) ON DELETE CASCADE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(1),
    UNIQUE(student_id, course_id)
);

-- ✅ Insert data
INSERT INTO teachers (name, email, department) VALUES
('Lars Larsson', 'lars@school.com', 'Matematik'),
('Karin Karlsson', 'karin@school.com', 'Svenska'),
('Eva Eriksson', 'eva@school.com', 'Datavetenskap');

INSERT INTO courses (name, credits, teacher_id) VALUES
('Matematik 1', 5, 1),
('Svenska 1', 3, 2),
('Programmering 1', 4, 3),
('Databasteknik', 5, 3);

INSERT INTO students (name, email, grade, department, enrollment_year) VALUES
('Anna Andersson', 'anna77@email.com', 'A', 'Datavetenskap', 2023),
('Erik Eriksson', 'erik99@email.com', 'B', 'Matematik', 2023),
('Maria Svensson', 'maria@email.com', 'A', 'Datavetenskap', 2022),
('Lars Nilsson', 'lars@email.com', 'C', 'Fysik', 2023),
('Karin Pettersson', 'karin@email.com', 'B', 'Svenska', 2022);



INSERT INTO enrollments (student_id, course_id, grade) VALUES
(1, 3, 'A'),   -- Anna (id=1)
(2, 1, 'B'),   -- Erik (id=2)
(7, 4, 'A'),   -- Anna again (id=7)
(8, 1, 'B'),   -- Erik again (id=8)
(9, 3, 'A'),   -- Maria (id=9)
(10, 1, 'C'),  -- Lars (id=10)
(11, 2, 'B');  -- Karin (id=11)

-- Check data
SELECT * FROM teachers;
SELECT * FROM courses;
SELECT * FROM students;
SELECT * FROM enrollments;


SELECT id, name FROM students;


SELECT name, email, grade FROM students;

SELECT DISTINCT department FROM students;
SELECT DISTINCT grade FROM students;

SELECT
    name,
    grade,
    enrollment_year,
    2024 - enrollment_year AS years_enrolled
FROM students;

-- Konkatenera text
SELECT
    name,
    email,
    name || ' (' || email || ')' AS full_info
FROM students;

SELECT 
    name, 
    email, 
    name || '(' || email || ')' as full_info
FROM students


SELECT
    name,
    grade,
    CASE
        WHEN grade = 'A' THEN 'Excellent'
        WHEN grade = 'B' THEN 'Very Good'
        WHEN grade = 'C' THEN 'Good'
        WHEN grade = 'D' THEN 'Satisfactory'
        WHEN grade = 'F' THEN 'Fail'
        ELSE 'No Grade'
    END AS grade_description
FROM students;



-- Översätt betyg till beskrivningar
SELECT
    name,
    grade, 
    CASE
        WHEN grade = 'A' THEN 'Excellent'
        WHEN grade = 'B' THEN 'Very Good'
        WHEN grade = 'C' THEN 'Good'
        WHEN grade = 'D' THEN 'Satisfactory'
        WHEN grade = 'F' THEN 'Fail'
        ELSE 'No Grade'
    END AS grade_description
FROM students

SELECT
    name,
    enrollment_year,
    CASE
        WHEN enrollment_year >= 2023 THEN 'First year'
        WHEN enrollment_year >= 2022 THEN 'Second year'
        WHEN enrollment_year >= 2021 THEN 'Third year'
        ELSE 'Senior'
    END AS year_level
FROM students;


-- Kategorisera studenter efter årskurs
SELECT
    name,
    enrollment_year,
    CASE
        WHEN enrollment_year >= 2023 THEN 'First year'
        WHEN enrollment_year >= 2022 THEN 'Second year'
        WHEN enrollment_year >= 2021 THEN 'Third year'
        ELSE 'Senior'
    END AS year_level
FROM students;

-- Alias (smeknamn för kolumner och tabeller)

-- Kolumn-alias med AS

SELECT
    name AS student_name,
    email AS student_email,
    grade AS final_grade
FROM students;

-- Alias utan AS (fungerar men mindre tydligt)
SELECT name student_name, email student_email FROM students;

-- Tabell-alias (användbart vid JOINs)
SELECT
    s.name,
    s.grade,
    s.department
FROM students s;  -- 's' är alias för students


-- Alias med mellanslag (kräver citattecken)
SELECT
    name AS "Student Name",
    grade AS "Final Grade"
FROM students;

-- ### WHERE-klausul och filtrering

-- Kunna filtrera data med WHERE

-- Grundläggande WHERE-operatorer

-- Jämförelseoperatorer
SELECT * FROM students WHERE grade = 'A';
SELECT * FROM students WHERE grade != 'F';  -- Inte F
SELECT * FROM students WHERE grade <> 'F';  -- Samma som !=
SELECT * FROM students WHERE enrollment_year > 2022;
SELECT * FROM students WHERE enrollment_year >= 2023;
SELECT * FROM students WHERE enrollment_year < 2023;
SELECT * FROM students WHERE enrollment_year <= 2022;

-- Numeriska jämförelser
SELECT * FROM courses WHERE credits > 3;
SELECT * FROM courses WHERE credits BETWEEN 3 AND 5;


-- Text-sökning med LIKE och ILIKE
-- LIKE (case-sensitive)
SELECT * FROM students WHERE name LIKE 'A%';      -- Börjar med A
SELECT * FROM students WHERE name LIKE '%son';    -- Slutar med son
SELECT * FROM students WHERE name LIKE '%er%';    -- Innehåller er
SELECT * FROM students WHERE name LIKE '_nna';    -- Andra bokstaven är n

-- ILIKE (case-insensitive, PostgreSQL-specifikt)
SELECT * FROM students WHERE name ILIKE 'anna%';  -- Matchar Anna, anna, ANNA
SELECT * FROM students WHERE email ILIKE '%@email.com';

-- Text-sökning med LIKE och ILIKE
-- LIKE (case-sensitive)
SELECT * FROM students WHERE name LIKE 'A%';      -- Börjar med A
SELECT * FROM students WHERE name LIKE '%son';    -- Slutar med son
SELECT * FROM students WHERE name LIKE '%er%';    -- Innehåller er
SELECT * FROM students WHERE name LIKE '_nna';    -- Andra bokstaven är n

-- ILIKE (case-insensitive, PostgreSQL-specifikt)
SELECT * FROM students WHERE name ILIKE 'anna%';  -- Matchar Anna, anna, ANNA
SELECT * FROM students WHERE email ILIKE '%@email.com';


-- NULL-hantering
-- Kontrollera NULL-värden
SELECT * FROM students WHERE email IS NULL;
SELECT * FROM students WHERE email IS NOT NULL;
SELECT * FROM students WHERE grade IS NULL;

-- NULL i beräkningar (NULL + anything = NULL)
SELECT
    name,
    enrollment_year,
    COALESCE(enrollment_year, 2024) AS year_with_default
FROM students;


-- Logiska operatorer (AND, OR, NOT)

-- AND - båda villkoren måste vara sanna
SELECT * FROM students
WHERE grade = 'A' AND department = 'Datavetenskap';

SELECT * FROM students
WHERE enrollment_year >= 2023 AND grade IN ('A', 'B');

-- OR - minst ett villkor måste vara sant
SELECT * FROM students
WHERE grade = 'A' OR grade = 'B';

SELECT * FROM students
WHERE department = 'Datavetenskap' OR department = 'Matematik';

-- NOT - negera villkor
SELECT * FROM students WHERE NOT grade = 'F';
SELECT * FROM students WHERE grade NOT IN ('D', 'F');

-- Kombinera AND och OR (använd parenteser!)
SELECT * FROM students
WHERE (grade = 'A' OR grade = 'B')
  AND enrollment_year >= 2023;


-- IN och BETWEEN

-- IN - matcha mot flera värden
SELECT * FROM students WHERE grade IN ('A', 'B', 'C');
SELECT * FROM students WHERE department IN ('Datavetenskap', 'Matematik');
SELECT * FROM students WHERE id IN (1, 3, 5, 7);

-- NOT IN
SELECT * FROM students WHERE grade NOT IN ('D', 'F');

-- BETWEEN - intervall (inklusivt)
SELECT * FROM students WHERE enrollment_year BETWEEN 2021 AND 2023;
SELECT * FROM courses WHERE credits BETWEEN 3 AND 5;

-- NOT BETWEEN
SELECT * FROM students WHERE enrollment_year NOT BETWEEN 2020 AND 2022;


-- ### Sortering med ORDER BY

-- Mål:** Kunna sortera resultat

-- Grundläggande ORDER BY

-- Stigande sortering (ASC är standard)
SELECT * FROM students ORDER BY name;
SELECT * FROM students ORDER BY name ASC;

-- Fallande sortering
SELECT * FROM students ORDER BY enrollment_year DESC;
SELECT * FROM students ORDER BY grade DESC;

-- Sortera på flera kolumner
SELECT * FROM students
ORDER BY grade ASC, name ASC;

SELECT * FROM students
ORDER BY department ASC, grade DESC, name ASC;

-- Sortera på kolumnposition (undvik i produktion)
SELECT name, grade, email
FROM students
ORDER BY 2, 1;  -- Sortera på grade (kolumn 2), sedan name (kolumn 1)


-- Sortering med NULL-värden
-- PostgreSQL: NULL sorteras sist vid ASC, först vid DESC
SELECT * FROM students ORDER BY email;

-- Kontrollera NULL-sortering explicit
SELECT * FROM students ORDER BY email NULLS FIRST;
SELECT * FROM students ORDER BY email NULLS LAST;


-- LIMIT och OFFSET (paginering)

-- Hämta första 5 raderna
SELECT * FROM students LIMIT 5;

-- Hämta topp 3 studenter med bäst betyg
SELECT * FROM students ORDER BY grade ASC LIMIT 3;

-- Paginering: hoppa över rader
SELECT * FROM students LIMIT 5 OFFSET 0;   -- Rad 1-5 (sida 1)
SELECT * FROM students LIMIT 5 OFFSET 5;   -- Rad 6-10 (sida 2)
SELECT * FROM students LIMIT 5 OFFSET 10;  -- Rad 11-15 (sida 3)

-- Kombinera med ORDER BY för konsekvent paginering
SELECT * FROM students
ORDER BY id
LIMIT 10 OFFSET 20;  -- Sida 3 (om 10 per sida)



-- Aggregeringsfunktioner

-- Kunna använda aggregeringsfunktioner för att analysera data

-- Grundläggande aggregeringsfunktioner

-- COUNT - räkna rader
SELECT COUNT(*) FROM students;                    -- Alla rader
SELECT COUNT(email) FROM students;                -- Icke-NULL värden
SELECT COUNT(DISTINCT department) FROM students;  -- Unika avdelningar

-- SUM - summera värden
SELECT SUM(credits) FROM courses;
SELECT SUM(credits) AS total_credits FROM courses;

-- AVG - genomsnitt
SELECT AVG(credits) FROM courses;
SELECT ROUND(AVG(credits), 2) AS avg_credits FROM courses;

-- MIN och MAX
SELECT MIN(enrollment_year) FROM students;  -- Tidigaste
SELECT MAX(enrollment_year) FROM students;  -- Senaste
SELECT MIN(grade) AS best_grade FROM students;
SELECT MAX(grade) AS worst_grade FROM students;

-- Flera aggregeringar samtidigt
SELECT
    COUNT(*) AS total_students,
    COUNT(DISTINCT department) AS total_departments,
    MIN(enrollment_year) AS oldest_enrollment,
    MAX(enrollment_year) AS newest_enrollment
FROM students;


-- GROUP BY - gruppera data

-- Räkna studenter per betyg
SELECT
    grade,
    COUNT(*) AS student_count
FROM students
GROUP BY grade
ORDER BY grade;

-- Räkna studenter per avdelning
SELECT
    department,
    COUNT(*) AS student_count
FROM students
GROUP BY department
ORDER BY student_count DESC;

-- Flera kolumner i GROUP BY
SELECT
    department,
    grade,
    COUNT(*) AS student_count
FROM students
GROUP BY department, grade
ORDER BY department, grade;

-- Aggregering per grupp
SELECT
    department,
    COUNT(*) AS total_students,
    MIN(enrollment_year) AS oldest_student_year,
    MAX(enrollment_year) AS newest_student_year
FROM students
GROUP BY department;


-- HAVING - filtrera grupperade resultat

-- HAVING filtrerar EFTER aggregering (WHERE filtrerar FÖRE)
-- Hitta avdelningar med fler än 2 studenter
SELECT
    department,
    COUNT(*) AS student_count
FROM students
GROUP BY department
HAVING COUNT(*) > 2
ORDER BY student_count DESC;

-- Hitta betyg som mer än 1 student har
SELECT
    grade,
    COUNT(*) AS count
FROM students
GROUP BY grade
HAVING COUNT(*) > 1
ORDER BY grade;

-- Kombinera WHERE och HAVING
SELECT
    department,
    COUNT(*) AS student_count
FROM students
WHERE enrollment_year >= 2022  -- WHERE filtrerar före gruppering
GROUP BY department
HAVING COUNT(*) >= 2           -- HAVING filtrerar efter gruppering
ORDER BY student_count DESC;




SELECT
    department,
    COUNT(*) AS total_students,
    MIN(enrollment_year) AS oldest_student_year,
    MAX(enrollment_year) AS newest_student_year
FROM students
GROUP BY department;


-- PostgreSQL-specifika funktioner
-- STRING_AGG - konkatenera värden i grupp
SELECT
    department,
    STRING_AGG(name, ', ' ORDER BY name) AS student_names
FROM students
GROUP BY department;

-- ARRAY_AGG - skapa array av värden
SELECT
    department,
    ARRAY_AGG(name ORDER BY name) AS student_array
FROM students
GROUP BY department;

-- COUNT med FILTER (PostgreSQL 9.4+)
SELECT
    department,
    COUNT(*) AS total,
    COUNT(*) FILTER (WHERE grade = 'A') AS a_grades,
    COUNT(*) FILTER (WHERE grade IN ('A', 'B')) AS ab_grades
FROM students
GROUP BY department;



-- 1. Visa alla studenter
SELECT * FROM students;

-- 2. Visa endast namn och betyg
SELECT name, grade FROM students;

-- 3. Visa studenter med betyg A
SELECT name, department, grade FROM students WHERE grade = 'A';

-- 4. Visa studenter vars namn börjar med 'A'
SELECT * FROM students WHERE name LIKE 'A%';

-- 5. Visa studenter utan email (om några saknas)
SELECT name, department FROM students WHERE email IS NULL;

-- 6. Visa studenter från Datavetenskap eller Matematik
SELECT name, department, grade
FROM students
WHERE department IN ('Datavetenskap', 'Matematik');
--------------------------------------------------------------------------------------

-- Vecka 45

-- Lägg till en rad
INSERT INTO students(name, email, grade, department, enrollment_year) VALUES
('Osman Camara', 'osse93@live.com', 'A', 'Databasteknik', 2024);

-- Lägg till flera rader på en gång (mer effektivt!)
INSERT INTO students(name, email, grade, department, enrollment_year) VALUES
('Samuel Bergström', 'samuel.bergstrom@example.com', 'A', 'AI-utveckling', 2024),
('Elina Holm', 'elina.holm@example.com', 'B', 'Systemvetenskap', 2023),
('Noah Lindgren', 'noah.lindgren@example.com', 'A', 'Datateknik', 2022);

-- PostgreSQL: RETURNING klausul (returnera den skapade raden)
INSERT INTO students (name, email, grade, department)
VALUES ('Jonas Åkesson', 'jonas.akesson@example.com', 'A', 'Programmering')
RETURNING *;  -- Returnera all data inkl. auto-genererat ID


-- Returnera endast specifika kolumner
INSERT INTO students (name, email, grade, department)
VALUES ('Johan Johansson', 'johan@email.com', 'A', 'Matematik')
RETURNING id, name, created_at;



-- INSERT med DEFAULT-värden
-- Låt databas sätta DEFAULT-värden
INSERT INTO students (name, email)
VALUES ('Eva Gustafsson', 'eva@email.com');
-- grade blir 'F' (DEFAULT), created_at blir CURRENT_TIMESTAMP

-- Explicit DEFAULT
INSERT INTO students (name, email, grade, created_at)
VALUES ('Peter Svensson', 'peter@email.com', DEFAULT, DEFAULT);

-- Sätt vissa kolumner, resten får DEFAULT
INSERT INTO students (name, email, department)
VALUES ('Sara Andersson', 'sara@email.com', 'Svenska');



-- INSERT med SELECT (kopiera data)
-- Kopiera data från en tabell till en annan
INSERT INTO students_backup (name, email, grade)
SELECT name, email, grade 
FROM students 
WHERE grade = 'A';

-- Skapa en "top students" tabell
CREATE TABLE top_students AS 
SELECT * FROM students WHERE grade = 'A';

-- Lägg till beräknade värden (statistik från flera tabeller)
-- Detta exempel visar hur man kan beräkna och lagra aggregerad data
INSERT INTO student_statistics (student_id, course_count, avg_grade)
SELECT 
    s.id,                    -- Student-ID från students-tabellen
    COUNT(e.id),             -- Räkna antal kurser studenten är registrerad på
    AVG(CASE                 -- Beräkna genomsnittligt betyg (konvertera bokstäver till siffror)
        WHEN e.grade = 'A' THEN 5
        WHEN e.grade = 'B' THEN 4
        WHEN e.grade = 'C' THEN 3
        WHEN e.grade = 'D' THEN 2
        ELSE 1               -- E eller NULL får värdet 1
    END)
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id  -- LEFT JOIN inkluderar alla studenter,
                                                 -- även de utan kurser
GROUP BY s.id;               -- Gruppera per student så vi får statistik för varje student

-- Förklaring steg för steg:
-- 1. Vi tar alla studenter från students-tabellen (s)
-- 2. Vi kopplar (LEFT JOIN) deras enrollments (e) - alla registrerade kurser
-- 3. För varje student (GROUP BY s.id) beräknar vi:
--    - Antal kurser: COUNT(e.id) räknar hur många enrollments studenten har
--    - Genomsnittsbetyg: AVG(CASE...) konverterar betygen A-E till 5-1 och beräknar medelvärdet
-- 4. Resultatet läggs in i student_statistics-tabellen

-------------------------Droped tables from above--------------------------------------------------  



-- OPTIONAL: only run once to create the DB
-- CREATE DATABASE school;

-- ===== Reset (safe re-run) =====
DROP TABLE IF EXISTS student_statistics CASCADE;
DROP TABLE IF EXISTS enrollments CASCADE;
DROP TABLE IF EXISTS courses CASCADE;
DROP TABLE IF EXISTS teachers CASCADE;
DROP TABLE IF EXISTS students_backup CASCADE;
DROP TABLE IF EXISTS top_students CASCADE;
DROP TABLE IF EXISTS students CASCADE;

-- ===== Created Tables =====

-- Students
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    grade VARCHAR(1) DEFAULT 'F',
    department VARCHAR(50),
    enrollment_year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Teachers
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    department VARCHAR(100)
);

-- Courses
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    credits INTEGER DEFAULT 3,
    teacher_id INTEGER REFERENCES teachers(id)
);

-- Enrollments (many-to-many)
CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    course_id  INTEGER REFERENCES courses(id)  ON DELETE CASCADE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(1),
    UNIQUE(student_id, course_id)
);

-- Backup table (structure only)
CREATE TABLE students_backup (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    grade VARCHAR(1) DEFAULT 'F'
);

-- Aggregated stats table you use later
CREATE TABLE student_statistics (
    student_id INTEGER PRIMARY KEY REFERENCES students(id) ON DELETE CASCADE,
    course_count INTEGER NOT NULL DEFAULT 0,
    avg_grade NUMERIC(3,2)
);

-- ===== Seed data (use ON CONFLICT to allow re-runs) =====

INSERT INTO teachers (name, email, department) VALUES
('Lars Larsson',  'lars@school.com',  'Matematik'),
('Karin Karlsson','karin@school.com', 'Svenska'),
('Eva Eriksson',  'eva@school.com',   'Datavetenskap')
ON CONFLICT DO NOTHING;

INSERT INTO courses (name, credits, teacher_id) VALUES
('Matematik 1',   5, 1),
('Svenska 1',     3, 2),
('Programmering 1',4, 3),
('Databasteknik', 5, 3)
ON CONFLICT DO NOTHING;

INSERT INTO students (name, email, grade, department, enrollment_year) VALUES
('Anna Andersson',  'anna77@email.com', 'A', 'Datavetenskap', 2023),
('Erik Eriksson',   'erik99@email.com', 'B', 'Matematik',     2023),
('Maria Svensson',  'maria@email.com',  'A', 'Datavetenskap', 2022),
('Lars Nilsson',    'lars@email.com',   'C', 'Fysik',         2023),
('Karin Pettersson','karin@email.com',  'B', 'Svenska',       2022)
ON CONFLICT (email) DO NOTHING;

-- ===== Enrollments without hard-coding IDs =====
-- Map by names to avoid FK problems
WITH data(student_name, course_name, grade) AS (
  VALUES
    ('Anna Andersson',  'Programmering 1', 'A'),
    ('Erik Eriksson',   'Matematik 1',     'B'),
    ('Maria Svensson',  'Programmering 1', 'A'),
    ('Lars Nilsson',    'Matematik 1',     'C'),
    ('Karin Pettersson','Svenska 1',       'B')
)
INSERT INTO enrollments (student_id, course_id, grade)
SELECT s.id, c.id, d.grade
FROM data d
JOIN students s ON s.name = d.student_name
JOIN courses  c ON c.name = d.course_name
ON CONFLICT (student_id, course_id) DO NOTHING;

-- ===== Examples you had =====

-- Backup only A-students
INSERT INTO students_backup (name, email, grade)
SELECT name, email, grade FROM students WHERE grade = 'A'
ON CONFLICT (email) DO NOTHING;

-- Snapshot table (optional)
CREATE TABLE top_students AS
SELECT * FROM students WHERE grade = 'A';

-- Compute stats into student_statistics
INSERT INTO student_statistics (student_id, course_count, avg_grade)
SELECT 
  s.id,
  COUNT(e.id),
  AVG(
     CASE e.grade
       WHEN 'A' THEN 5
       WHEN 'B' THEN 4
       WHEN 'C' THEN 3
       WHEN 'D' THEN 2
       ELSE 1
     END
  )::NUMERIC(3,2)
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.id
GROUP BY s.id
ON CONFLICT (student_id) DO UPDATE
SET course_count = EXCLUDED.course_count,
    avg_grade    = EXCLUDED.avg_grade;

-- Quick checks
SELECT id, name FROM students ORDER BY id;
SELECT * FROM enrollments ORDER BY student_id, course_id;




-- ON CONFLICT (PostgreSQL UPSERT)

-- Hantera konflikter vid INSERT
INSERT INTO students (id, name, email, grade) 
VALUES (1, 'Anna Andersson', 'anna@email.com', 'A')
ON CONFLICT (id) DO NOTHING;  -- Gör inget om ID finns

-- Uppdatera vid konflikt (UPSERT = UPDATE + INSERT)
-- EXCLUDED är ett speciellt nyckelord som refererar till de NYA värden vi försökte INSERT:a
INSERT INTO students (id, name, email, grade, department) 
VALUES (1, 'Anna Andersson', 'anna.new@email.com', 'A', 'Datavetenskap')
ON CONFLICT (id)              -- Om student med id=1 redan finns...
DO UPDATE SET 
    email = EXCLUDED.email,           -- ...använd nya emailet ('anna.new@email.com')
    grade = EXCLUDED.grade,           -- ...använd nya betyget ('A')
    department = EXCLUDED.department; -- ...använd nya avdelningen ('Datavetenskap')

-- Förklaring av EXCLUDED:
-- EXCLUDED.email innehåller värdet 'anna.new@email.com' (från VALUES-satsen)
-- Det är alltså de värden vi FÖRSÖKTE lägga till, men som inte gick pga konflikt
-- Vi kan sedan välja vilka av dessa värden vi vill uppdatera den befintliga raden med

-- ON CONFLICT med unique constraint (email)
INSERT INTO students (name, email, grade) 
VALUES ('Test User', 'anna@email.com', 'B')
ON CONFLICT (email)           -- Om email 'anna@email.com' redan finns...
DO UPDATE SET 
    grade = EXCLUDED.grade;   -- ...uppdatera betyget till det nya värdet ('B')
                              -- EXCLUDED.grade = 'B' (från VALUES)
                              -- EXCLUDED.name = 'Test User' (från VALUES)






--  UPDATE - Uppdatera data

-- Mål:** Kunna ändra befintlig data

-- Grundläggande UPDATE

-- Uppdatera en rad (VIKTIGT: alltid med WHERE!)
UPDATE students
SET grade = 'B'
WHERE id = 1;

-- Uppdatera flera kolumner
UPDATE students
SET
    grade = 'A',
    department = 'Datavetenskap',
    email = 'anna.new@email.com'
WHERE id = 1;

-- Uppdatera alla rader som matchar villkor
UPDATE students
SET grade = 'F'
WHERE grade IS NULL;

-- Uppdatera med beräkningar
UPDATE courses
SET credits = credits + 1
WHERE credits < 5;

-- Uppdatera baserat på annat fält
UPDATE students
SET department = 'Unknown'
WHERE department IS NULL;


-- UPDATE med CASE

-- Villkorlig uppdatering
UPDATE students SET grade =
    CASE
        WHEN grade = 'A' THEN 'S'
        WHEN grade = 'B' THEN 'A'
        WHEN grade = 'C' THEN 'B'
        ELSE grade
    END
WHERE department = 'Datavetenskap';

-- Uppdatera baserat på flera villkor
UPDATE students SET department =
    CASE
        WHEN name LIKE '%son' THEN 'Swedish'
        WHEN enrollment_year < 2022 THEN 'Senior'
        ELSE department
    END;




--  UPDATE med JOIN (PostgreSQL FROM syntax)

-- Uppdatera baserat på data från annan tabell
UPDATE students s
SET department = t.department
FROM teachers t
WHERE s.name = t.name;

-- Uppdatera med subquery
UPDATE students
SET grade = 'A'
WHERE id IN (
    SELECT student_id
    FROM enrollments
    WHERE grade = 'A' AND course_id = 1
);

-- Mer komplex UPDATE med JOIN
UPDATE courses c
SET credits = c.credits + 1
FROM teachers t
WHERE c.teacher_id = t.id
  AND t.department = 'Datavetenskap';


-- UPDATE med RETURNING

-- Se vad som uppdaterades
UPDATE students
SET grade = 'A'
WHERE department = 'Datavetenskap' AND grade = 'B'
RETURNING id, name, grade;

-- Räkna antal uppdaterade rader
WITH updated AS (
    UPDATE students
    SET grade = 'B'
    WHERE grade = 'C'
    RETURNING *
)
SELECT COUNT(*) AS updated_count FROM updated;




-- DELETE - Ta bort data

-- *Mål:** Kunna ta bort data från databasen

-- Grundläggande DELETE

-- Ta bort en specifik rad (alltid med WHERE!)
DELETE FROM students WHERE id = 1;

-- Ta bort flera rader
DELETE FROM students WHERE grade = 'F';

-- Ta bort med flera villkor
DELETE FROM students
WHERE enrollment_year < 2020 AND grade IS NULL;

-- FARLIGT: Ta bort alla rader (använd TRUNCATE istället)
DELETE FROM students;  -- Raderar alla rader (långsamt)

-- TRUNCATE - snabbare för att tömma tabell
TRUNCATE students;  -- Nollställer hela tabellen
TRUNCATE students RESTART IDENTITY;  -- Återställer även ID-räknaren
TRUNCATE students CASCADE;  -- Raderar även relaterad data



-- DELETE med subquery

-- Ta bort studenter som inte har några registreringar
DELETE FROM students
WHERE id NOT IN (
    SELECT DISTINCT student_id
    FROM enrollments
);

-- Ta bort med EXISTS
DELETE FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM enrollments e
    WHERE e.student_id = s.id
);

-- Ta bort baserat på aggregat
DELETE FROM students
WHERE id IN (
    SELECT student_id
    FROM enrollments
    GROUP BY student_id
    HAVING COUNT(*) < 2
);


-- DELETE med RETURNING

-- Se vad som togs bort
DELETE FROM students
WHERE grade = 'F'
RETURNING id, name, email;

-- Flytta data innan borttagning (arkivering)
WITH deleted AS (
    DELETE FROM students
    WHERE enrollment_year < 2020
    RETURNING *
)
INSERT INTO students_archive
SELECT * FROM deleted;


-- The CTE = common table expression. creates with clause "WITH" 
-- then a choosen name "deleted" in this case,
-- that stores the result of the deletion here:.
-- It is a temporry table that only exists during the execution of the query..
WITH deleted AS (
    DELETE FROM students
    WHERE enrollment_year < 2020
    RETURNING *
)
INSERT INTO students_archive
SELECT * FROM deleted;




-- Relationer och främmande nycklar

-- Mål:** Förstå och implementera relationer mellan tabeller

-- One-to-Many relation


-- En lärare kan ha många kurser
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(50)
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    credits INTEGER DEFAULT 3,
    teacher_id INTEGER REFERENCES teachers(id) ON DELETE SET NULL
    -- ON DELETE SET NULL: Om lärare tas bort, sätt teacher_id till NULL
    -- ON DELETE CASCADE: Om lärare tas bort, ta även bort kursen
    -- ON DELETE RESTRICT: Tillåt inte borttagning om kurser finns
);

-- Lägg till data
INSERT INTO teachers (name, email, department) VALUES
('Lars Larsson', 'lars@school.com', 'Matematik'),
('Karin Karlsson', 'karin@school.com', 'Svenska');

INSERT INTO courses (name, credits, teacher_id) VALUES
('Matematik 1', 5, 1),
('Matematik 2', 5, 1),
('Svenska 1', 3, 2);



-------------------------------------------------
-- ON DELETE och ON UPDATE actions

-- Olika alternativ för främmande nycklar
CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id)
        ON DELETE CASCADE        -- Ta bort enrollment om student tas bort
        ON UPDATE CASCADE,       -- Uppdatera om student ID ändras
    course_id INTEGER REFERENCES courses(id)
        ON DELETE RESTRICT       -- Förhindra borttagning av kurs om enrollments finns
        ON UPDATE CASCADE
);

-- Exempel på effekter:
-- ON DELETE CASCADE: Raderar relaterade rader
DELETE FROM students WHERE id = 1;  -- Raderar även studentens enrollments

-- ON DELETE SET NULL: Sätter FK till NULL
-- ON DELETE SET DEFAULT: Sätter FK till DEFAULT-värde
-- ON DELETE RESTRICT: Förhindrar borttagning
-- ON DELETE NO ACTION: Samma som RESTRICT (PostgreSQL default)

---------------------------------------------
-- JOIN-operationer

-- Mål:** Kunna hämta data från flera tabeller samtidigt

-- INNER JOIN - endast matchande rader

-- Hämta studenter med deras kurser
SELECT
    s.name AS student_name,
    c.name AS course_name,
    e.grade
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id
INNER JOIN courses c ON e.course_id = c.id
ORDER BY s.name, c.name;

-- Kort syntax (JOIN = INNER JOIN)
SELECT s.name, c.name, e.grade
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id;

-- Flera JOIN-villkor
SELECT t.name AS teacher, c.name AS course
FROM teachers t
INNER JOIN courses c ON t.id = c.teacher_id AND c.credits > 3;



-- LEFT JOIN - alla från vänster tabell

-- Visa alla studenter, även de utan kurser
SELECT
    s.name AS student_name,
    c.name AS course_name,
    e.grade
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
LEFT JOIN courses c ON e.course_id = c.id
ORDER BY s.name;

-- Hitta studenter som INTE har några kurser
SELECT s.name, s.email
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.id IS NULL;

-- Räkna kurser per student (inkl. 0 kurser)
SELECT
    s.name,
    COUNT(e.id) AS course_count
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
GROUP BY s.id, s.name
ORDER BY course_count DESC;


SELECT 
    s.name AS student_name,
    c.name AS course_name,
    e.grade 
FROM students s 
LEFT JOIN enrollments e on s.id = e.student_id
LEFT JOIN courses c ON e.course_id = c.id


SELECT s.name, s.email
FROM students s 
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.id IS NULL;




SELECT 
    s.name,
    COUNT(e.id) as course_count
FROM students s 
LEFT JOIN enrollments e ON s.id = e.student_id
GROUP BY s.id, s.name
ORDER BY course_count DESC; 




-- RIGHT JOIN - alla från höger tabell

-- Visa alla kurser, även de utan studenter
SELECT
    c.name AS course_name,
    s.name AS student_name
FROM enrollments e
RIGHT JOIN courses c ON e.course_id = c.id
LEFT JOIN students s ON e.student_id = s.id
ORDER BY c.name;

-- Hitta kurser utan studenter
SELECT c.name AS empty_course
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
WHERE e.id IS NULL;


-- FULL OUTER JOIN - alla från båda tabeller

-- Visa alla studenter och kurser, inkl. orphans
SELECT
    s.name AS student,
    c.name AS course
FROM students s
FULL OUTER JOIN enrollments e ON s.id = e.student_id
FULL OUTER JOIN courses c ON e.course_id = c.id;



SELECT 
    s.name AS student,
    c.course AS course
FROM students s 
FULL OUTER JOIN enrollments e ON s.id =e.student_id
FULL OUTER JOIN courses c ON e.course_id = c.id;



--------------------------------------------------------------------


-- Laboration: CRUD-operationer och relationer i PostgreSQL
-- Förberedelse: Skapa databas
-- Med pgAdmin:
-- Öppna pgAdmin och anslut till school databasen
-- Öppna Query Tool
-- Kör följande SQL för att återskapa tabellerna:

DROP TABLE IF EXISTS enrollments, courses, teachers, students CASCADE;

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    grade VARCHAR(1) DEFAULT 'F',
    department VARCHAR(50),
    enrollment_year INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    credits INTEGER DEFAULT 3,
    teacher_id INTEGER REFERENCES teachers(id) ON DELETE SET NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE enrollments (
    id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    course_id INTEGER REFERENCES courses(id) ON DELETE CASCADE,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    grade VARCHAR(1),
    UNIQUE(student_id, course_id)
);



-- Uppgift 1: INSERT-operationer


-- 1. Lägg till lärare med RETURNING
INSERT INTO teachers (name, email, department) VALUES
('Lars Larsson', 'lars@school.com', 'Matematik'),
('Karin Karlsson', 'karin@school.com', 'Svenska'),
('Eva Eriksson', 'eva@school.com', 'Datavetenskap')
RETURNING id, name;

-- 2. Lägg till kurser
INSERT INTO courses (name, credits, teacher_id) VALUES
('Matematik 1', 5, 1),
('Svenska 1', 3, 2),
('Programmering 1', 4, 3);

-- 3. Lägg till studenter (flera på en gång)
INSERT INTO students (name, email, grade, department, enrollment_year) VALUES
('Anna Andersson', 'anna@email.com', 'A', 'Datavetenskap', 2023),
('Erik Eriksson', 'erik@email.com', 'B', 'Matematik', 2023),
('Maria Svensson', 'maria@email.com', 'A', 'Datavetenskap', 2022);

-- 4. Registrera studenter för kurser
INSERT INTO enrollments (student_id, course_id, grade) VALUES
(1, 3, 'A'),
(2, 1, 'B'),
(3, 3, 'A');

-- 5. Testa ON CONFLICT (UPSERT)
INSERT INTO students (id, name, email, grade)
VALUES (1, 'Anna Andersson', 'anna@email.com', 'S')
ON CONFLICT (id) DO UPDATE SET grade = EXCLUDED.grade
RETURNING *;




-- Uppgift 2: UPDATE-operationer

-- Med pgAdmin Query Tool:**

-- 1. Uppdatera en students betyg
UPDATE students
SET grade = 'S'
WHERE name = 'Anna Andersson'
RETURNING *;

-- 2. Uppdatera alla studenter från ett visst år
UPDATE students
SET enrollment_year = 2024
WHERE enrollment_year = 2023
RETURNING name, enrollment_year;

-- 3. Öka credits för alla kurser
UPDATE courses
SET credits = credits + 1
WHERE credits < 5;

-- 4. Uppdatera baserat på JOIN
UPDATE students s
SET department = t.department
FROM teachers t
WHERE s.name LIKE t.name || '%';

-- 5. Villkorlig uppdatering med CASE
UPDATE students SET grade =
    CASE
        WHEN grade = 'B' THEN 'A'
        WHEN grade = 'C' THEN 'B'
        ELSE grade
    END
WHERE department = 'Datavetenskap';





-- Uppgift 2: UPDATE-operationer

-- *Med pgAdmin Query Tool:**


-- 1. Uppdatera en students betyg
UPDATE students
SET grade = 'S'
WHERE name = 'Anna Andersson'
RETURNING *;

-- 2. Uppdatera alla studenter från ett visst år
UPDATE students
SET enrollment_year = 2024
WHERE enrollment_year = 2023
RETURNING name, enrollment_year;

-- 3. Öka credits för alla kurser
UPDATE courses
SET credits = credits + 1
WHERE credits < 5;

-- 4. Uppdatera baserat på JOIN
UPDATE students s
SET department = t.department
FROM teachers t
WHERE s.name LIKE t.name || '%';

-- 5. Villkorlig uppdatering med CASE
UPDATE students SET grade =
    CASE
        WHEN grade = 'B' THEN 'A'
        WHEN grade = 'C' THEN 'B'
        ELSE grade
    END
WHERE department = 'Datavetenskap';


UPDATE students s
SET department = t.department
FROM teachers t
WHERE s.name LIKE t.name || '%';



-- Uppgift 3: DELETE-operationer

-- *Med pgAdmin Query Tool:**


-- 1. Ta bort en specifik enrollment
DELETE FROM enrollments
WHERE student_id = 2 AND course_id = 1
RETURNING *;

-- 2. Ta bort studenter med betyg F (om några finns)
DELETE FROM students
WHERE grade = 'F'
RETURNING name, email;

-- 3. Testa CASCADE - ta bort student
DELETE FROM students WHERE id = 3;
-- Kontrollera att enrollments också försvann
SELECT * FROM enrollments WHERE student_id = 3;

-- 4. Ta bort kurser utan studenter
DELETE FROM courses
WHERE id NOT IN (SELECT DISTINCT course_id FROM enrollments)
RETURNING name;




DELETE FROM courses
WHERE id NOT IN (SELECT DISTINCT course_id FROM enrollments)
RETURNING name;



-- Uppgift 4: JOIN-queries


-- 1. Visa alla studenter med deras kurser
SELECT
    s.name AS student,
    c.name AS course,
    e.grade,
    t.name AS teacher
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id
JOIN teachers t ON c.teacher_id = t.id
ORDER BY s.name;

-- 2. Räkna kurser per student (inkl. 0)
SELECT
    s.name,
    COUNT(e.id) AS courses_taken
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
GROUP BY s.id, s.name
ORDER BY courses_taken DESC;

-- 3. Hitta kurser utan studenter
SELECT c.name AS empty_course
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
WHERE e.id IS NULL;

-- 4. Genomsnittligt betyg per kurs
SELECT
    c.name AS course,
    COUNT(e.id) AS student_count,
    STRING_AGG(DISTINCT e.grade, ', ') AS grades
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
GROUP BY c.id, c.name
ORDER BY student_count DESC;



SELECT
    c.name AS empty_course
    from courses c
    left JOIN enrollment e ON c.id = ecourse_id
    WHERE e.id IS NULL;






-------------------------------------------------------------------------

-- Vecka 45 - Torsdag: Avancerade JOINs, Subqueries, Views och Index

-- Lektionens syfte

-- I denna lektion fördjupar vi oss i avancerade SQL-koncept: komplexa JOINs, subqueries, views för att förenkla queries, och index för prestandaoptimering.

-- 1. Avancerade JOIN-operationer

-- Mål:** Behärska komplexa JOIN-scenarier

-- SELF JOIN - koppla tabell med sig själv


-- Hitta studenter med samma betyg
SELECT
    s1.name AS student1,
    s2.name AS student2,
    s1.grade
FROM students s1
INNER JOIN students s2 ON s1.grade = s2.grade AND s1.id < s2.id
ORDER BY s1.grade, s1.name;

-- Hitta studenter från samma avdelning
SELECT
    s1.name AS student1,
    s2.name AS student2,
    s1.department
FROM students s1
INNER JOIN students s2
    ON s1.department = s2.department
    AND s1.id < s2.id
ORDER BY s1.department;

-- Organisationshierarki (chef-anställd)
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    manager_id INTEGER REFERENCES employees(id)
);

-- Hitta anställda med deras chefer
SELECT
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;





--CROSS JOIN - kartesisk produkt

-- Alla kombinationer av studenter och kurser
SELECT
    s.name AS student,
    c.name AS course
FROM students s
CROSS JOIN courses c
ORDER BY s.name, c.name;

-- Användbart för att skapa all möjliga kombinationer
SELECT
    d.day_name,
    t.time_slot
FROM days d
CROSS JOIN time_slots t;



-- Multiple JOINs i samma query

-- Komplex query med flera JOINs
SELECT
    s.name AS student_name,
    s.department AS student_dept,
    c.name AS course_name,
    c.credits,
    t.name AS teacher_name,
    t.department AS teacher_dept,
    e.grade,
    e.enrollment_date
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id
INNER JOIN courses c ON e.course_id = c.id
LEFT JOIN teachers t ON c.teacher_id = t.id
WHERE s.grade IN ('A', 'B')
ORDER BY s.name, c.name;



-- JOIN med aggregering

-- Räkna studenter per lärare
SELECT
    t.name AS teacher,
    t.department,
    COUNT(DISTINCT c.id) AS course_count,
    COUNT(DISTINCT e.student_id) AS student_count
FROM teachers t
LEFT JOIN courses c ON t.id = c.teacher_id
LEFT JOIN enrollments e ON c.id = e.course_id
GROUP BY t.id, t.name, t.department
ORDER BY student_count DESC;

-- Genomsnittligt betyg per avdelning per kurs
SELECT
    s.department,
    c.name AS course,
    COUNT(e.id) AS enrollments,
    STRING_AGG(DISTINCT e.grade, ', ') AS grades
FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id
GROUP BY s.department, c.id, c.name
HAVING COUNT(e.id) >= 2
ORDER BY s.department, enrollments DESC;




-- ### Subqueries (nested queries)

-- Mål:** Förstå och använda subqueries effektivt

-- Subquery i WHERE-klausul


-- Hitta studenter som tar samma kurs som Anna
SELECT name, email
FROM students
WHERE id IN (
    SELECT DISTINCT student_id
    FROM enrollments
    WHERE course_id IN (
        SELECT course_id
        FROM enrollments e
        JOIN students s ON e.student_id = s.id
        WHERE s.name = 'Anna Andersson'
    )
) AND name != 'Anna Andersson';

-- Studenter med fler kurser än genomsnittet
SELECT name,
    (SELECT COUNT(*) FROM enrollments WHERE student_id = s.id) AS course_count
FROM students s
WHERE (
    SELECT COUNT(*)
    FROM enrollments
    WHERE student_id = s.id
) > (
    SELECT AVG(course_count)
    FROM (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_courses
);

-- Studenter som INTE har tagit någon kurs
SELECT name, email
FROM students
WHERE id NOT IN (
    SELECT DISTINCT student_id
    FROM enrollments
);

