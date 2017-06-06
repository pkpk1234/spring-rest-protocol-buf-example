package com.example.protocolbuf.controller;

import com.example.protocolbuf.CompanyProto;
import com.example.protocolbuf.ImageProto;
import com.example.protocolbuf.ImporterProto;
import com.example.protocolbuf.ProductProto;
import com.example.protocolbuf.repository.ProductRepository;
import com.example.protocolbuf.store.Image;
import com.example.protocolbuf.store.Product;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Set;

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

    @GetMapping("/firstprod")
    public ProductProto.Product first() {
        return prepareProtoProduct(this.productRepository.findOne(1L)).build();
    }

    @GetMapping("/products")
    public List<ProductProto.Product> getAllProducts() {
        Collection<Product> products = this.productRepository.findAll();
        List<ProductProto.Product> result = new ArrayList<>(products.size());
        prepareProtoProduct(products, result);
        return result;
    }

    private void prepareProtoProduct(Collection<Product> products, List<ProductProto.Product> result) {
        for (Product product : products) {
            ProductProto.Product.Builder builder = prepareProtoProduct(product);
            result.add(builder.build());
        }
    }

    private ProductProto.Product.Builder prepareProtoProduct(Product product) {
        ProductProto.Product.Builder builder = ProductProto.Product.newBuilder();
        builder.setCode(product.getCode());
        builder.setCompany(CompanyProto.Company.newBuilder().setName(product.getCompany().getName()));
        builder.setImporter(ImporterProto.Importer.newBuilder().setName(product.getImporter().getName()));
        builder.setQuantity(product.getQuantity());
        buildProtoImages(product, builder);
        return builder;
    }

    private void buildProtoImages(Product product, ProductProto.Product.Builder builder) {
        Set<Image> images = product.getImages();
        for (Image image : images) {
            builder.addImage(ImageProto.Image.newBuilder().setIndex(image.getIndex()).setName(image.getName()).build());
        }
    }

}
