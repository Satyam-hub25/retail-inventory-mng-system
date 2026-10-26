package com.retail.inventory.service;

import com.retail.inventory.model.Product;
import com.retail.inventory.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.transaction.annotation.Transactional;
import java.util.List;
import java.util.Optional;

@Service
public class ProductService {

    @Autowired
    private ProductRepository repository;

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public List<Product> getAll() {
        return repository.findAll();
    }

    public List<Product> getByCategoryId(Long categoryId) {
        return repository.findByCategoryId(categoryId);
    }

    public List<Product> getBySupplierId(Long supplierId) {
        return repository.findBySupplierId(supplierId);
    }

    public List<Product> searchByName(String name) {
        return repository.findByNameContainingIgnoreCase(name);
    }

    public Optional<Product> getById(Long id) {
        return repository.findById(id);
    }

    public Product create(Product product) {
        return repository.save(product);
    }

    public Product update(Long id, Product productDetails) {
        Optional<Product> optional = repository.findById(id);
        if (optional.isPresent()) {
            Product existing = optional.get();
            existing.setName(productDetails.getName());
            existing.setSku(productDetails.getSku());
            existing.setDescription(productDetails.getDescription());
            existing.setPrice(productDetails.getPrice());
            existing.setImageUrl(productDetails.getImageUrl());
            existing.setCategory(productDetails.getCategory());
            existing.setSupplier(productDetails.getSupplier());
            return repository.save(existing);
        }
        return null;
    }

    @Transactional
    public void delete(Long id) {
        jdbcTemplate.update("DELETE FROM order_items WHERE product_id = ?", id);
        jdbcTemplate.update("DELETE FROM purchase_order_items WHERE product_id = ?", id);
        jdbcTemplate.update("DELETE FROM stock_movements WHERE product_id = ?", id);
        jdbcTemplate.update("DELETE FROM inventory WHERE product_id = ?", id);
        repository.deleteById(id);
    }
}
