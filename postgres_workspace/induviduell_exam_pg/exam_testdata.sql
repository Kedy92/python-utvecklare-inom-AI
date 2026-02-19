-- ============================================
-- Testdata för Electronics DB
-- ============================================

-- ============================================
-- Brands (Tillverkare)
-- ============================================
INSERT INTO brands (name, country, founded_year, description) VALUES
('Apple', 'USA', 1976, 'Premium electronics and innovative technology'),
('Samsung', 'South Korea', 1938, 'Global leader in electronics and semiconductors'),
('Sony', 'Japan', 1946, 'Entertainment and technology pioneer'),
('Dell', 'USA', 1984, 'Computer hardware and enterprise solutions'),
('Lenovo', 'China', 1984, 'PC and mobile device manufacturer');

-- ============================================
-- Products (Produkter)
-- ============================================
INSERT INTO products (name, brand_id, sku, release_year, price, warranty_months, category, stock_quantity) VALUES
-- Apple products
('iPhone 15 Pro', 1, 'APL-IP15P-BLK', 2023, 12999.00, 12, 'Smartphones', 45),
('MacBook Pro 16"', 1, 'APL-MBP16-SLV', 2023, 29999.00, 12, 'Laptops', 15),
('iPad Air', 1, 'APL-IPAD-AIR', 2022, 6999.00, 12, 'Tablets', 30),
('AirPods Pro', 1, 'APL-AIRP-PRO', 2023, 2799.00, 12, 'Audio', 100),

-- Samsung products
('Galaxy S24 Ultra', 2, 'SAM-GS24U-BLK', 2024, 13499.00, 24, 'Smartphones', 60),
('Galaxy Book3', 2, 'SAM-GB3-GRY', 2023, 12999.00, 24, 'Laptops', 25),
('Galaxy Tab S9', 2, 'SAM-TAB-S9', 2023, 8999.00, 24, 'Tablets', 40),

-- Sony products
('PlayStation 5', 3, 'SNY-PS5-STD', 2020, 5999.00, 12, 'Gaming', 80),
('WH-1000XM5', 3, 'SNY-WH1000XM5', 2022, 3999.00, 24, 'Audio', 50),
('Bravia XR A80L', 3, 'SNY-TV-A80L', 2023, 19999.00, 24, 'TVs', 10),

-- Dell products
('XPS 15', 4, 'DEL-XPS15-9530', 2023, 16999.00, 12, 'Laptops', 20),
('Alienware m18', 4, 'DEL-ALW-M18', 2024, 34999.00, 12, 'Laptops', 8),

-- Lenovo products
('ThinkPad X1 Carbon', 5, 'LEN-X1C-G11', 2023, 18999.00, 36, 'Laptops', 18),
('Legion 5 Pro', 5, 'LEN-LEG5P-2023', 2023, 14999.00, 24, 'Laptops', 22);

-- ============================================
-- Customers (Kunder)
-- ============================================
INSERT INTO customers (first_name, last_name, email, phone, city, registration_date) VALUES
('Erik', 'Andersson', 'erik.andersson@email.se', '0701234567', 'Stockholm', '2023-01-15'),
('Anna', 'Karlsson', 'anna.karlsson@email.se', '0702345678', 'Göteborg', '2023-03-20'),
('Johan', 'Nilsson', 'johan.nilsson@email.se', '0703456789', 'Malmö', '2023-06-10'),
('Maria', 'Svensson', 'maria.svensson@email.se', '0704567890', 'Uppsala', '2023-09-05'),
('Lars', 'Johansson', 'lars.johansson@email.se', '0705678901', 'Stockholm', '2024-01-12'),
('Sofia', 'Berg', 'sofia.berg@email.se', '0706789012', 'Lund', '2024-02-28'),
('Gustav', 'Lindström', 'gustav.lindstrom@email.se', '0707890123', 'Linköping', '2024-05-15');

-- ============================================
-- Orders (Beställningar)
-- ============================================
INSERT INTO orders (customer_id, order_date, status, shipping_city) VALUES
(1, '2024-01-10', 'completed', 'Stockholm'),
(2, '2024-02-14', 'completed', 'Göteborg'),
(1, '2024-03-20', 'completed', 'Stockholm'),
(3, '2024-04-05', 'completed', 'Malmö'),
(4, '2024-05-12', 'completed', 'Uppsala'),
(5, '2024-06-18', 'completed', 'Stockholm'),
(2, '2024-07-22', 'completed', 'Göteborg'),
(6, '2024-08-30', 'completed', 'Lund'),
(1, '2024-09-15', 'pending', 'Stockholm'),
(7, '2024-10-20', 'pending', 'Linköping'),
(3, '2024-11-01', 'pending', 'Malmö'),
(4, '2024-11-10', 'cancelled', 'Uppsala');

-- ============================================
-- Order_Items (Beställningsrader)
-- ============================================
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
-- Order 1: Erik köper iPhone och AirPods
(1, 1, 1, 12999.00),
(1, 4, 1, 2799.00),

-- Order 2: Anna köper Samsung laptop
(2, 6, 1, 12999.00),

-- Order 3: Erik köper MacBook
(3, 2, 1, 29999.00),

-- Order 4: Johan köper PlayStation och hörlurar
(4, 8, 1, 5999.00),
(4, 9, 1, 3999.00),

-- Order 5: Maria köper Galaxy S24
(5, 5, 1, 13499.00),

-- Order 6: Lars köper iPad och Dell XPS
(6, 3, 1, 6999.00),
(6, 11, 1, 16999.00),

-- Order 7: Anna köper Samsung Tab
(7, 7, 2, 8999.00),

-- Order 8: Sofia köper Lenovo laptop
(8, 13, 1, 18999.00),

-- Order 9: Erik köper Sony TV (pending)
(9, 10, 1, 19999.00),

-- Order 10: Gustav köper gaming laptop (pending)
(10, 12, 1, 34999.00),

-- Order 11: Johan köper ThinkPad (pending)
(11, 13, 1, 18999.00),

-- Order 12: Maria köper Galaxy phone (cancelled)
(12, 5, 1, 13499.00);

-- Uppdatera total_amount för varje order
UPDATE orders o
SET total_amount = (
    SELECT SUM(quantity * unit_price)
    FROM order_items oi
    WHERE oi.order_id = o.id
);

-- ============================================
-- Reviews (Recensioner)
-- ============================================
INSERT INTO reviews (product_id, customer_id, rating, comment, review_date) VALUES
-- iPhone reviews
(1, 1, 5, 'Fantastisk telefon! Kameran är otrolig.', '2024-01-20'),
(1, 5, 4, 'Mycket bra, men lite dyr.', '2024-06-25'),

-- MacBook reviews
(2, 1, 5, 'Bästa laptopen jag ägt. Superkraftig!', '2024-04-01'),

-- Galaxy S24 reviews
(5, 4, 5, 'Älskar den stora skärmen och batterilivslängden.', '2024-05-20'),
(5, 3, 4, 'Riktigt bra telefon men lite tung.', '2024-08-15'),

-- PlayStation 5 reviews
(8, 3, 5, 'Gaming i toppklass! Värt varje krona.', '2024-04-15'),

-- Sony headphones reviews
(9, 3, 5, 'Bästa noise-cancelling jag testat.', '2024-04-20'),

-- Dell XPS reviews
(11, 5, 4, 'Snygg design och bra prestanda.', '2024-07-01'),

-- Samsung Tab reviews
(7, 2, 4, 'Perfekt för både jobb och nöje.', '2024-08-01'),

-- Lenovo ThinkPad reviews
(13, 6, 5, 'Professionell laptop med fantastiskt tangentbord.', '2024-09-10'),
(13, 7, 5, 'Pålitlig och kraftfull. Perfekt för arbete.', '2024-11-01');

-- ============================================
-- Verifiera data
-- ============================================
-- SELECT * FROM brands;
-- SELECT * FROM products;
-- SELECT * FROM customers;
-- SELECT * FROM orders;
-- SELECT * FROM order_items;
-- SELECT * FROM reviews;