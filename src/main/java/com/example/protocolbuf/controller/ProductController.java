package com.example.protocolbuf.controller;

import com.example.protocolbuf.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by pkpk1234 on 2017/6/5.
 */

@RestController
public class ProductController {
    private final ProductRepository productRepository;

    @Autowired
    public ProductController(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    //@GetMapping("/products")

}
