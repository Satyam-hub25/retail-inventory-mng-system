-- Add image_url column to products table if not present
ALTER TABLE products ADD COLUMN IF NOT EXISTS image_url VARCHAR(1000);

-- Update products with accurate, high-resolution product images
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=600&q=80' WHERE sku = 'MOB-PRO-01';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&w=600&q=80' WHERE sku = 'AUD-WEB-02';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-KBD-03';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1580481077195-731da0671607?auto=format&fit=crop&w=600&q=80' WHERE sku = 'OFF-CHR-04';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-MON-05';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=600&q=80' WHERE sku = 'AUD-SPK-06';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-LST-07';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1583863788434-e58a36330cf0?auto=format&fit=crop&w=600&q=80' WHERE sku = 'MOB-CHG-08';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80' WHERE sku = 'AUD-HDP-09';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-LPT-10';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-MOU-11';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1595515106969-1ce29566ff1c?auto=format&fit=crop&w=600&q=80' WHERE sku = 'OFF-DSK-12';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80' WHERE sku = 'MOB-SMW-13';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1587826080692-f439cd0b70da?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-CAM-14';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1561154464-82e9adf32764?auto=format&fit=crop&w=600&q=80' WHERE sku = 'MOB-TAB-15';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1584438784894-089d6a62b8fa?auto=format&fit=crop&w=600&q=80' WHERE sku = 'OFF-ORG-16';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1609592426868-80e2279fa693?auto=format&fit=crop&w=600&q=80' WHERE sku = 'MOB-PBK-17';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?auto=format&fit=crop&w=600&q=80' WHERE sku = 'AUD-MIC-18';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1597872200969-2b65d56bd16b?auto=format&fit=crop&w=600&q=80' WHERE sku = 'CMP-SSD-19';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1612815154858-60aa4c59eaa6?auto=format&fit=crop&w=600&q=80' WHERE sku = 'OFF-PRN-20';

-- Default test seed products
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=600&q=80' WHERE sku = 'TECH-LPT-001';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80' WHERE sku = 'TECH-AUD-002';
UPDATE products SET image_url = 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=600&q=80' WHERE sku = 'APP-TSH-001';

