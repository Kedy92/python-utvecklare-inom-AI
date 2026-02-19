-- ============================================
-- Electronics DB Schema
-- Databas för elektronikbutik
-- ============================================

-- Skapa databasen (kör separat om behövs)
CREATE DATABASE electronics_db;

-- Anslut till databasen
-- \c electronics_db;

-- Drop tables if they exist (i rätt ordning p.g.a. foreign keys)
DROP TABLE IF EXISTS reviews CASCADE;
DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS brands CASCADE;

-- ============================================
-- Brands (Tillverkare)
-- ============================================
CREATE TABLE brands (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    founded_year INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- Products (Produkter)
-- ============================================
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    brand_id INTEGER NOT NULL,
    sku VARCHAR(50) UNIQUE,
    release_year INTEGER,
    price DECIMAL(10, 2) NOT NULL,
    warranty_months INTEGER,
    category VARCHAR(50),
    stock_quantity INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign key
    CONSTRAINT fk_brand
        FOREIGN KEY (brand_id)
        REFERENCES brands(id)
        ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT check_price_positive
        CHECK (price > 0),
    CONSTRAINT check_stock_non_negative
        CHECK (stock_quantity >= 0)
);

-- Index för bättre prestanda vid sökningar
CREATE INDEX idx_products_brand_id ON products(brand_id);
CREATE INDEX idx_products_category ON products(category);

-- ============================================
-- Customers (Kunder)
-- ============================================
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(100),
    registration_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index för e-post lookups
CREATE INDEX idx_customers_email ON customers(email);

-- ============================================
-- Orders (Beställningar)
-- ============================================
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount DECIMAL(10, 2),
    status VARCHAR(20) DEFAULT 'pending',
    shipping_city VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign key
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE CASCADE,
    
    -- Check constraint
    CONSTRAINT check_status_valid
        CHECK (status IN ('pending', 'completed', 'cancelled'))
);

-- Index för vanliga sökningar
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_order_date ON orders(order_date);
CREATE INDEX idx_orders_status ON orders(status);

-- ============================================
-- Order_Items (Beställningsrader)
-- ============================================
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign keys
    CONSTRAINT fk_order
        FOREIGN KEY (order_id)
        REFERENCES orders(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE CASCADE,
    
    -- Check constraints
    CONSTRAINT check_quantity_positive
        CHECK (quantity > 0),
    CONSTRAINT check_unit_price_positive
        CHECK (unit_price > 0)
);

-- Index för joins
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);

-- ============================================
-- Reviews (Recensioner)
-- ============================================
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    comment TEXT,
    review_date DATE DEFAULT CURRENT_DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign keys
    CONSTRAINT fk_review_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_review_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(id)
        ON DELETE CASCADE,
    
    -- Check constraint för rating
    CONSTRAINT check_rating_range
        CHECK (rating >= 1 AND rating <= 5)
);

-- Index för vanliga queries
CREATE INDEX idx_reviews_product_id ON reviews(product_id);
CREATE INDEX idx_reviews_customer_id ON reviews(customer_id);

-- ============================================
-- Visa alla tabeller och deras struktur
-- ============================================
-- \dt
-- \d brands
-- \d products
-- \d customers
-- \d orders
-- \d order_items
-- \d reviews



