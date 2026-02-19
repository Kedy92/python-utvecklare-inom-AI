-- ============================================
-- SQL Queries - G-nivå
-- 10 queries som demonstrerar grundläggande SQL
-- ============================================

-- ============================================
-- GRUNDLÄGGANDE QUERIES (4 st)
-- ============================================

-- Query 1: Hämta alla produkter sorterade efter namn
-- Visar alla produkter i alfabetisk ordning
SELECT 
    id,
    name,
    price,
    category,
    stock_quantity
FROM products
ORDER BY name ASC;


-- Query 2: Hämta alla produkter som kostar mer än 5000 kr
-- Användbart för att filtrera dyra produkter
SELECT 
    name,
    price,
    category,
    warranty_months
FROM products
WHERE price > 5000
ORDER BY price DESC;


-- Query 3: Hämta alla beställningar från 2024
-- Visar årets beställningar för analys
SELECT 
    id,
    customer_id,
    order_date,
    total_amount,
    status,
    shipping_city
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = 2024
ORDER BY order_date DESC;


-- Query 4: Hämta alla pending beställningar
-- Viktigt för att se vilka ordrar som behöver hanteras
SELECT 
    o.id AS order_id,
    o.order_date,
    c.first_name || ' ' || c.last_name AS customer_name,
    o.total_amount,
    o.shipping_city
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.status = 'pending'
ORDER BY o.order_date;


-- ============================================
-- JOIN-QUERIES (3 st)
-- ============================================

-- Query 5: Visa alla produkter med deras tillverkares namn
-- Kombinerar produkt- och tillverkarinformation
SELECT 
    p.name AS product_name,
    b.name AS brand_name,
    p.price,
    p.category,
    b.country AS brand_country
FROM products p
JOIN brands b ON p.brand_id = b.id
ORDER BY b.name, p.name;


-- Query 6: Visa alla beställningar med kundens namn och totalt belopp
-- Ger en komplett överblick över orders och kunder
SELECT 
    o.id AS order_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    c.email,
    o.order_date,
    o.total_amount,
    o.status,
    o.shipping_city
FROM orders o
JOIN customers c ON o.customer_id = c.id
ORDER BY o.order_date DESC;


-- Query 7: Visa vilka produkter varje kund har köpt
-- Detaljerad vy över kundernas köphistorik
SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    p.name AS product_name,
    b.name AS brand_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) AS total_price,
    o.order_date
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
JOIN brands b ON p.brand_id = b.id
ORDER BY c.last_name, o.order_date;


-- ============================================
-- AGGREGERING OCH ANALYS (3 st)
-- ============================================

-- Query 8: Räkna antal produkter per tillverkare
-- Visar vilka brands som har flest produkter i sortimentet
SELECT 
    b.name AS brand_name,
    COUNT(p.id) AS number_of_products,
    AVG(p.price) AS average_price,
    MIN(p.price) AS cheapest_product,
    MAX(p.price) AS most_expensive_product
FROM brands b
LEFT JOIN products p ON b.id = p.brand_id
GROUP BY b.id, b.name
ORDER BY number_of_products DESC;


-- Query 9: Hitta kunder som har spenderat mest totalt
-- Identifierar de mest värdefulla kunderna (VIP-kunder)
SELECT 
    c.id,
    c.first_name || ' ' || c.last_name AS customer_name,
    c.email,
    c.city,
    COUNT(o.id) AS number_of_orders,
    SUM(o.total_amount) AS total_spent,
    AVG(o.total_amount) AS average_order_value
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.status = 'completed'
GROUP BY c.id, c.first_name, c.last_name, c.email, c.city
ORDER BY total_spent DESC;


-- Query 10: Visa produkter med genomsnittligt betyg från recensioner
-- Hjälper att identifiera populära och välrecenserade produkter
SELECT 
    p.name AS product_name,
    b.name AS brand_name,
    p.price,
    COUNT(r.id) AS number_of_reviews,
    ROUND(AVG(r.rating), 2) AS average_rating,
    MIN(r.rating) AS lowest_rating,
    MAX(r.rating) AS highest_rating
FROM products p
JOIN brands b ON p.brand_id = b.id
LEFT JOIN reviews r ON p.id = r.product_id
GROUP BY p.id, p.name, b.name, p.price
HAVING COUNT(r.id) > 0
ORDER BY average_rating DESC, number_of_reviews DESC;


-- ============================================
-- BONUS QUERIES (Extra användbar information)
-- ============================================

-- Bonus Query 1: Produkter med lågt lagersaldo (behöver beställas)
SELECT 
    p.name AS product_name,
    b.name AS brand_name,
    p.stock_quantity,
    p.category
FROM products p
JOIN brands b ON p.brand_id = b.id
WHERE p.stock_quantity < 20
ORDER BY p.stock_quantity ASC;


-- Bonus Query 2: Mest sålda produkter
SELECT 
    p.name AS product_name,
    b.name AS brand_name,
    SUM(oi.quantity) AS total_sold,
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
JOIN brands b ON p.brand_id = b.id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE o.status = 'completed'
GROUP BY p.id, p.name, b.name
ORDER BY total_sold DESC
LIMIT 5;