-- ============================================================
--  SALES DATABASE — COMPLETE QUERY COLLECTION
--  Tables: products | customers | orders | order_items
-- ============================================================


-- ============================================================
-- 1. SIMPLE QUERIES
-- ============================================================

-- 1.1  All products — names and prices only
SELECT name, price
FROM products;

-- 1.2  All customers
SELECT * FROM customers;

-- 1.3  Distinct product categories
SELECT DISTINCT category
FROM products;

-- 1.4  First 10 products
SELECT * FROM products
LIMIT 10;


-- ============================================================
-- 2. CONDITIONAL QUERIES
-- ============================================================

-- 2.1  Products priced above 50
SELECT * FROM products
WHERE price > 50;

-- 2.2  Customers from Baku
SELECT * FROM customers
WHERE city = 'Baku';

-- 2.3  Products in the Electronics category
SELECT * FROM products
WHERE category = 'electronics';

-- 2.4  Orders created after 2024-01-01
SELECT * FROM orders
WHERE created_at > '2024-01-01';

-- 2.5  Customers whose email ends with @gmail.com
SELECT * FROM customers
WHERE email LIKE '%@gmail.com';

-- 2.6  Products priced between 20 and 80
SELECT * FROM products
WHERE price BETWEEN 20 AND 80;

-- 2.7  Products NOT in the Clothing category
SELECT * FROM products
WHERE category <> 'clothing';


-- ============================================================
-- 3. AGGREGATE FUNCTIONS
-- ============================================================

-- 3.1  Total number of products
SELECT COUNT(*) AS total_products
FROM products;

-- 3.2  Average product price
SELECT ROUND(AVG(price), 2) AS avg_price
FROM products;

-- 3.3  Total number of customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- 3.4  Sum of all sold item quantities
SELECT SUM(quantity) AS total_items_sold
FROM order_items;

-- 3.5  Number of orders each customer has made
SELECT
    c.full_name,
    COUNT(o.id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.full_name
ORDER BY order_count DESC;

-- 3.6  Highest priced product
SELECT name, price
FROM products
ORDER BY price DESC
LIMIT 1;

-- 3.7  Number of products per category
SELECT
    category,
    COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;


-- ============================================================
-- 4. JOIN QUERIES
-- ============================================================

-- 4.1  All orders with the customer's full name
SELECT
    o.id         AS order_id,
    c.full_name,
    o.created_at
FROM orders o
JOIN customers c ON c.id = o.customer_id
ORDER BY o.created_at;

-- 4.2  Each ordered product: name, quantity, order date
SELECT
    p.name           AS product_name,
    oi.quantity,
    o.created_at     AS order_date
FROM order_items oi
JOIN orders   o ON o.id  = oi.order_id
JOIN products p ON p.id  = oi.product_id
ORDER BY o.created_at;

-- 4.3  Total items purchased per customer
SELECT
    c.full_name,
    COALESCE(SUM(oi.quantity), 0) AS total_items
FROM customers c
LEFT JOIN orders      o  ON o.customer_id = c.id
LEFT JOIN order_items oi ON oi.order_id   = o.id
GROUP BY c.id, c.full_name
ORDER BY total_items DESC;

-- 4.4  Total amount spent per customer  (price × quantity)
SELECT
    c.full_name,
    ROUND(COALESCE(SUM(p.price * oi.quantity), 0), 2) AS total_spent
FROM customers c
LEFT JOIN orders      o  ON o.customer_id = c.id
LEFT JOIN order_items oi ON oi.order_id   = o.id
LEFT JOIN products    p  ON p.id          = oi.product_id
GROUP BY c.id, c.full_name
ORDER BY total_spent DESC;

-- 4.5  All orders (with product details) placed in 2024
SELECT
    o.id         AS order_id,
    c.full_name,
    p.name       AS product_name,
    p.category,
    oi.quantity,
    p.price,
    ROUND(p.price * oi.quantity, 2) AS line_total,
    o.created_at AS order_date
FROM orders o
JOIN customers    c  ON c.id  = o.customer_id
JOIN order_items  oi ON oi.order_id   = o.id
JOIN products     p  ON p.id          = oi.product_id
WHERE strftime('%Y', o.created_at) = '2024'
ORDER BY o.created_at;

-- 4.6  Customers who have NEVER placed an order
SELECT c.full_name, c.email, c.city
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- 4.7  Top 5 customers by total items purchased
SELECT
    c.full_name,
    COALESCE(SUM(oi.quantity), 0) AS total_items
FROM customers c
LEFT JOIN orders      o  ON o.customer_id = c.id
LEFT JOIN order_items oi ON oi.order_id   = o.id
GROUP BY c.id, c.full_name
ORDER BY total_items DESC
LIMIT 5;
