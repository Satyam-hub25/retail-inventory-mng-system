import random
from datetime import datetime, timedelta

# Set random seed for deterministic generation
random.seed(42)

categories = ['Electronics', 'Computer Accessories', 'Mobile Accessories', 'Office Equipment', 'Audio']
suppliers = [
    ('Reliance Retail Tech', 'contact@reliancetech.in', '022-555-0001'),
    ('Tata Croma Distribution', 'wholesale@croma.in', '022-555-0002'),
    ('Delhi Electronics Hub', 'sales@delhielectronics.in', '011-555-0003'),
    ('Bangalore IT Supply', 'info@blritsupply.in', '080-555-0004'),
    ('Chennai Gadget Wholesalers', 'orders@chennaigadgets.in', '044-555-0005')
]
warehouses = [
    ('Mumbai Central Warehouse', 'Andheri East, Mumbai, MH'),
    ('Delhi NCR Distribution Hub', 'Gurugram, HR'),
    ('Bangalore Tech Park Storage', 'Whitefield, Bangalore, KA'),
    ('Chennai Port Logistics', 'Chennai, TN')
]

products = [
    ('Smartphone Pro Max', 'MOB-PRO-01', 'High-end flagship smartphone', 85000.00, 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80', 'Mobile Accessories', 'Reliance Retail Tech'),
    ('Wireless Earbuds Elite', 'AUD-WEB-02', 'Noise-cancelling wireless earbuds', 12500.00, 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=600&q=80', 'Audio', 'Tata Croma Distribution'),
    ('Mechanical Keyboard V2', 'CMP-KBD-03', 'RGB mechanical gaming keyboard', 5500.00, 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Delhi Electronics Hub'),
    ('Office Ergonomic Chair', 'OFF-CHR-04', 'Adjustable office chair', 8500.00, 'https://images.unsplash.com/photo-1580481077195-731da0671607?auto=format&fit=crop&w=600&q=80', 'Office Equipment', 'Bangalore IT Supply'),
    ('4K Ultra HD Monitor', 'CMP-MON-05', '32-inch 4K display', 32000.00, 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Tata Croma Distribution'),
    ('Bluetooth Speaker Boom', 'AUD-SPK-06', 'Portable waterproof speaker', 4500.00, 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=600&q=80', 'Audio', 'Chennai Gadget Wholesalers'),
    ('Laptop Stand Aluminum', 'CMP-LST-07', 'Foldable premium laptop stand', 1800.00, 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Delhi Electronics Hub'),
    ('USB-C Fast Charger 65W', 'MOB-CHG-08', 'Multi-port fast wall charger', 2200.00, 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=600&q=80', 'Mobile Accessories', 'Reliance Retail Tech'),
    ('Noise Cancelling Headphones', 'AUD-HDP-09', 'Over-ear premium headphones', 18500.00, 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80', 'Audio', 'Tata Croma Distribution'),
    ('Business Laptop 14"', 'CMP-LPT-10', 'Thin and light business laptop', 65000.00, 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Bangalore IT Supply'),
    ('Wireless Mouse Ergo', 'CMP-MOU-11', 'Ergonomic wireless mouse', 1500.00, 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Delhi Electronics Hub'),
    ('Standing Desk Motorized', 'OFF-DSK-12', 'Height adjustable standing desk', 28000.00, 'https://images.unsplash.com/photo-1595515106969-1ce29566ff1c?auto=format&fit=crop&w=600&q=80', 'Office Equipment', 'Bangalore IT Supply'),
    ('Smartwatch Series X', 'MOB-SMW-13', 'Fitness tracking smartwatch', 15000.00, 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80', 'Mobile Accessories', 'Reliance Retail Tech'),
    ('Webcam 1080p HD', 'CMP-CAM-14', 'HD streaming webcam with mic', 3500.00, 'https://images.unsplash.com/photo-1587826080692-f439cd0b70da?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Chennai Gadget Wholesalers'),
    ('Tablet 10-inch Plus', 'MOB-TAB-15', '10.4 inch media tablet', 24000.00, 'https://images.unsplash.com/photo-1561154464-82e9adf32764?auto=format&fit=crop&w=600&q=80', 'Mobile Accessories', 'Reliance Retail Tech'),
    ('Desk Organizer Mesh', 'OFF-ORG-16', 'Metal mesh desk organizer', 800.00, 'https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?auto=format&fit=crop&w=600&q=80', 'Office Equipment', 'Bangalore IT Supply'),
    ('Power Bank 20000mAh', 'MOB-PBK-17', 'High capacity fast charging bank', 2500.00, 'https://images.unsplash.com/photo-1609592426868-80e2279fa693?auto=format&fit=crop&w=600&q=80', 'Mobile Accessories', 'Chennai Gadget Wholesalers'),
    ('Studio Microphone USB', 'AUD-MIC-18', 'Condenser microphone for podcasting', 7500.00, 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=600&q=80', 'Audio', 'Tata Croma Distribution'),
    ('External SSD 1TB', 'CMP-SSD-19', 'Portable NVMe solid state drive', 9500.00, 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=600&q=80', 'Computer Accessories', 'Delhi Electronics Hub'),
    ('Laser Printer Wireless', 'OFF-PRN-20', 'Monochrome laser printer', 14000.00, 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?auto=format&fit=crop&w=600&q=80', 'Office Equipment', 'Bangalore IT Supply')
]

customers = [
    ('Rajesh Kumar', 'rajesh.k@example.in', '9876543210'),
    ('Priya Sharma', 'priya.s@example.in', '9876543211'),
    ('Amit Patel', 'amit.p@example.in', '9876543212'),
    ('Sneha Reddy', 'sneha.r@example.in', '9876543213'),
    ('Vikram Singh', 'vikram.s@example.in', '9876543214'),
    ('Neha Gupta', 'neha.g@example.in', '9876543215')
]

sql = []
sql.append("TRUNCATE TABLE stock_movements, purchase_order_items, purchase_orders, order_items, orders, inventory, products, categories, suppliers, warehouses, customers RESTART IDENTITY CASCADE;")

sql.append("-- Categories")
for c in categories:
    sql.append(f"INSERT INTO categories (name, description) VALUES ('{c}', '{c} items');")

sql.append("-- Suppliers")
for s in suppliers:
    sql.append(f"INSERT INTO suppliers (name, contact_email, contact_phone) VALUES ('{s[0]}', '{s[1]}', '{s[2]}');")

sql.append("-- Warehouses")
for w in warehouses:
    sql.append(f"INSERT INTO warehouses (name, location) VALUES ('{w[0]}', '{w[1]}');")

sql.append("-- Customers")
for c in customers:
    sql.append(f"INSERT INTO customers (name, email, phone) VALUES ('{c[0]}', '{c[1]}', '{c[2]}');")

sql.append("-- Products")
for p in products:
    sql.append(f"INSERT INTO products (name, sku, description, price, image_url, category_id, supplier_id) VALUES ('{p[0]}', '{p[1]}', '{p[2]}', {p[3]}, '{p[4]}', (SELECT id FROM categories WHERE name='{p[5]}'), (SELECT id FROM suppliers WHERE name='{p[6]}'));")

sql.append("-- Inventory")
for p in products:
    for w in warehouses:
        qty = random.randint(10, 150)
        if random.random() < 0.2: qty = random.randint(0, 10) # low stock
        sql.append(f"INSERT INTO inventory (product_id, warehouse_id, quantity, reorder_level) VALUES ((SELECT id FROM products WHERE sku='{p[1]}'), (SELECT id FROM warehouses WHERE name='{w[0]}'), {qty}, 15);")
        
        # Initial Stock Movement
        sql.append(f"INSERT INTO stock_movements (product_id, warehouse_id, type, quantity, movement_date) VALUES ((SELECT id FROM products WHERE sku='{p[1]}'), (SELECT id FROM warehouses WHERE name='{w[0]}'), 'PURCHASE', {qty}, CURRENT_TIMESTAMP - INTERVAL '{random.randint(10,30)} days');")

sql.append("-- Orders and Order Items")
statuses = ['PENDING', 'PROCESSING', 'SHIPPED', 'DELIVERED']
for i in range(1, 26):
    c = random.choice(customers)
    status = random.choice(statuses)
    days_ago = random.randint(1, 15)
    
    # We will pick 1-3 products for this order
    num_items = random.randint(1, 3)
    order_items = random.sample(products, num_items)
    
    total_amount = 0
    items_sql = []
    
    for item in order_items:
        qty = random.randint(1, 5)
        price = item[3]
        total_amount += qty * price
        
        items_sql.append(f"INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES ({i}, (SELECT id FROM products WHERE sku='{item[1]}'), {qty}, {price});")
        
        if status in ['SHIPPED', 'DELIVERED']:
            # Subtract from inventory
            w = random.choice(warehouses)
            sql.append(f"UPDATE inventory SET quantity = quantity - {qty} WHERE product_id = (SELECT id FROM products WHERE sku='{item[1]}') AND warehouse_id = (SELECT id FROM warehouses WHERE name='{w[0]}');")
            sql.append(f"INSERT INTO stock_movements (product_id, warehouse_id, type, quantity, movement_date) VALUES ((SELECT id FROM products WHERE sku='{item[1]}'), (SELECT id FROM warehouses WHERE name='{w[0]}'), 'SALE', {qty}, CURRENT_TIMESTAMP - INTERVAL '{days_ago} days');")
            
    sql.append(f"INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES ((SELECT id FROM customers WHERE email='{c[1]}'), CURRENT_TIMESTAMP - INTERVAL '{days_ago} days', '{status}', {total_amount});")
    sql.extend(items_sql)

sql.append("-- Purchase Orders")
po_statuses = ['PENDING', 'SHIPPED', 'RECEIVED']
for i in range(1, 11):
    s = random.choice(suppliers)
    status = random.choice(po_statuses)
    days_ago = random.randint(1, 10)
    
    # Supplier supplies specific products
    supplier_products = [p for p in products if p[6] == s[0]]
    if not supplier_products: continue
    
    num_items = random.randint(1, min(3, len(supplier_products)))
    po_items = random.sample(supplier_products, num_items)
    
    total_amount = 0
    items_sql = []
    
    for item in po_items:
        qty = random.randint(20, 100)
        cost_price = item[3] * 0.7 # 30% margin
        total_amount += qty * cost_price
        
        items_sql.append(f"INSERT INTO purchase_order_items (purchase_order_id, product_id, quantity, unit_price) VALUES ({i}, (SELECT id FROM products WHERE sku='{item[1]}'), {qty}, {cost_price});")
        
    sql.append(f"INSERT INTO purchase_orders (supplier_id, order_date, status, total_amount) VALUES ((SELECT id FROM suppliers WHERE name='{s[0]}'), CURRENT_TIMESTAMP - INTERVAL '{days_ago} days', '{status}', {total_amount});")
    sql.extend(items_sql)


with open('retail-india-seed.sql', 'w') as f:
    f.write('\n'.join(sql))

print("SQL generated successfully!")
