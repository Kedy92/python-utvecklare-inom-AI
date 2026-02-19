CREATE DATABASE Receptdatabas;


CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    prep_time_minutes INTEGER CHECK (prep_time_minutes >= 0),
    cook_time_minutes INTEGER CHECK (cook_time_minutes >= 0),
    servings INTEGER CHECK (servings > 0),
    difficulty VARCHAR(10) CHECK (difficulty IN ('easy', 'medium', 'hard')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE ingredients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    unit VARCHAR(20),
    calories_per_unit DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE recipe_ingredients (
    id SERIAL PRIMARY KEY,
    recipe_id INTEGER REFERENCES recipes(id) ON DELETE CASCADE,
    ingredient_id INTEGER REFERENCES ingredients(id) ON DELETE CASCADE,
    quantity DECIMAL(10,2) CHECK (quantity > 0),
    UNIQUE(recipe_id, ingredient_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Testdata
INSERT INTO recipes (name, description, prep_time_minutes, cook_time_minutes, servings, difficulty) VALUES
('Pasta Carbonara', 'Klassisk italiensk pastarätt', 10, 15, 4, 'easy'),
('Pannkakor', 'Svenska pannkakor', 5, 20, 4, 'easy'),
('Beef Wellington', 'Lyxig kötträtt', 45, 60, 4, 'hard');

INSERT INTO ingredients (name, unit, calories_per_unit) VALUES
('Pasta', 'gram', 1.50),
('Ägg', 'st', 70.00),
('Bacon', 'gram', 5.00),
('Parmesan', 'gram', 4.00),
('Mjöl', 'dl', 360.00),
('Mjölk', 'dl', 64.00),
('Oxfilé', 'gram', 2.50),
('Smördeg', 'gram', 3.20);

INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES
-- Carbonara
(1, 1, 400),  -- 400g pasta
(1, 2, 4),    -- 4 ägg
(1, 3, 200),  -- 200g bacon
(1, 4, 100),  -- 100g parmesan
-- Pannkakor
(2, 2, 3),    -- 3 ägg
(2, 5, 3),    -- 3 dl mjöl
(2, 6, 6),    -- 6 dl mjölk
-- Beef Wellington
(3, 7, 800),  -- 800g oxfilé
(3, 8, 500),  -- 500g smördeg
(3, 2, 2);    -- 2 ägg

-- Verifiera
SELECT * FROM recipes;
SELECT * FROM ingredients;
SELECT * FROM recipe_ingredients;
