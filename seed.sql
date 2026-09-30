-- Categories
INSERT INTO categories (name, description) VALUES
('Electronics', 'Gadgets and devices'),
('Apparel', 'Clothing and accessories')
ON CONFLICT DO NOTHING;

-- Suppliers
INSERT INTO suppliers (name, contact_email, contact_phone) VALUES
('TechCorp Inc.', 'sales@techcorp.demo', '555-0199'),
('Fashion Forward', 'hello@fashion.demo', '555-0200')
ON CONFLICT DO NOTHING;

-- Warehouses
INSERT INTO warehouses (name, location) VALUES
('Main Hub', 'New York, NY'),
('West Coast Facility', 'Los Angeles, CA')
ON CONFLICT DO NOTHING;

-- Products (assuming IDs 1 and 2 for categories and suppliers)
INSERT INTO products (name, sku, description, price, category_id, supplier_id) VALUES
('ProBook 15"', 'TECH-LPT-001', 'High performance laptop', 1299.99, 
 (SELECT id FROM categories WHERE name = 'Electronics'), 
 (SELECT id FROM suppliers WHERE name = 'TechCorp Inc.')),
('Noise Cancelling Headphones', 'TECH-AUD-002', 'Over-ear wireless headphones', 199.50,
 (SELECT id FROM categories WHERE name = 'Electronics'), 
 (SELECT id FROM suppliers WHERE name = 'TechCorp Inc.')),
('Classic Cotton T-Shirt', 'APP-TSH-001', '100% cotton casual t-shirt', 24.99,
 (SELECT id FROM categories WHERE name = 'Apparel'), 
 (SELECT id FROM suppliers WHERE name = 'Fashion Forward'))
ON CONFLICT DO NOTHING;

-- Inventory
INSERT INTO inventory (product_id, warehouse_id, quantity, last_updated) VALUES
((SELECT id FROM products WHERE sku = 'TECH-LPT-001'), (SELECT id FROM warehouses WHERE name = 'Main Hub'), 50, CURRENT_TIMESTAMP),
((SELECT id FROM products WHERE sku = 'TECH-AUD-002'), (SELECT id FROM warehouses WHERE name = 'West Coast Facility'), 200, CURRENT_TIMESTAMP)
ON CONFLICT DO NOTHING;

-- Stock Movements
INSERT INTO stock_movements (product_id, warehouse_id, type, quantity, movement_date) VALUES
((SELECT id FROM products WHERE sku = 'TECH-LPT-001'), (SELECT id FROM warehouses WHERE name = 'Main Hub'), 'PURCHASE', 50, CURRENT_TIMESTAMP - INTERVAL '2 days'),
((SELECT id FROM products WHERE sku = 'TECH-AUD-002'), (SELECT id FROM warehouses WHERE name = 'West Coast Facility'), 'PURCHASE', 200, CURRENT_TIMESTAMP - INTERVAL '1 day')
ON CONFLICT DO NOTHING;
