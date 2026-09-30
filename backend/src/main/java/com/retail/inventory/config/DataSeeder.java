package com.retail.inventory.config;

import com.retail.inventory.model.*;
import com.retail.inventory.repository.*;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Configuration
public class DataSeeder {

    @Bean
    CommandLineRunner initDatabase(
            CategoryRepository categoryRepo,
            SupplierRepository supplierRepo,
            WarehouseRepository warehouseRepo,
            ProductRepository productRepo,
            InventoryRepository inventoryRepo,
            StockMovementRepository movementRepo) {
            
        return args -> {
            if (categoryRepo.count() == 0) {
                System.out.println("Seeding demo data...");

                // Categories
                Category electronics = new Category();
                electronics.setName("Electronics");
                electronics.setDescription("Gadgets and devices");
                categoryRepo.save(electronics);

                Category apparel = new Category();
                apparel.setName("Apparel");
                apparel.setDescription("Clothing and accessories");
                categoryRepo.save(apparel);

                // Suppliers
                Supplier techSupplier = new Supplier();
                techSupplier.setName("TechCorp Inc.");
                techSupplier.setContactEmail("sales@techcorp.demo");
                techSupplier.setContactPhone("555-0199");
                supplierRepo.save(techSupplier);

                Supplier fashionSupplier = new Supplier();
                fashionSupplier.setName("Fashion Forward");
                fashionSupplier.setContactEmail("hello@fashion.demo");
                fashionSupplier.setContactPhone("555-0200");
                supplierRepo.save(fashionSupplier);

                // Warehouses
                Warehouse mainHub = new Warehouse();
                mainHub.setName("Main Hub");
                mainHub.setLocation("New York, NY");
                warehouseRepo.save(mainHub);

                Warehouse westCoast = new Warehouse();
                westCoast.setName("West Coast Facility");
                westCoast.setLocation("Los Angeles, CA");
                warehouseRepo.save(westCoast);

                // Products
                Product laptop = new Product();
                laptop.setName("ProBook 15\"");
                laptop.setSku("TECH-LPT-001");
                laptop.setDescription("High performance laptop");
                laptop.setPrice(new BigDecimal("1299.99"));
                laptop.setCategory(electronics);
                laptop.setSupplier(techSupplier);
                productRepo.save(laptop);

                Product headphones = new Product();
                headphones.setName("Noise Cancelling Headphones");
                headphones.setSku("TECH-AUD-002");
                headphones.setDescription("Over-ear wireless headphones");
                headphones.setPrice(new BigDecimal("199.50"));
                headphones.setCategory(electronics);
                headphones.setSupplier(techSupplier);
                productRepo.save(headphones);

                Product tshirt = new Product();
                tshirt.setName("Classic Cotton T-Shirt");
                tshirt.setSku("APP-TSH-001");
                tshirt.setDescription("100% cotton casual t-shirt");
                tshirt.setPrice(new BigDecimal("24.99"));
                tshirt.setCategory(apparel);
                tshirt.setSupplier(fashionSupplier);
                productRepo.save(tshirt);

                // Inventory
                Inventory invLaptop = new Inventory();
                invLaptop.setProduct(laptop);
                invLaptop.setWarehouse(mainHub);
                invLaptop.setQuantity(50);
                inventoryRepo.save(invLaptop);

                Inventory invHeadphones = new Inventory();
                invHeadphones.setProduct(headphones);
                invHeadphones.setWarehouse(westCoast);
                invHeadphones.setQuantity(200);
                inventoryRepo.save(invHeadphones);

                // Add some initial stock movements to reflect the initial balance
                StockMovement mv1 = new StockMovement();
                mv1.setProduct(laptop);
                mv1.setWarehouse(mainHub);
                mv1.setQuantity(50);
                mv1.setType("PURCHASE");
                
                mv1.setMovementDate(LocalDateTime.now().minusDays(2));
                movementRepo.save(mv1);

                StockMovement mv2 = new StockMovement();
                mv2.setProduct(headphones);
                mv2.setWarehouse(westCoast);
                mv2.setQuantity(200);
                mv2.setType("PURCHASE");
                
                mv2.setMovementDate(LocalDateTime.now().minusDays(1));
                movementRepo.save(mv2);

                System.out.println("Demo data seeded successfully!");
            }
        };
    }
}
