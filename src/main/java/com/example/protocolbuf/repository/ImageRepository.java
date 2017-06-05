package com.example.protocolbuf.repository;

import com.example.protocolbuf.store.Image;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by pkpk1234 on 2017/6/3.
 */
@Repository
public interface ImageRepository extends JpaRepository<Image,Long> {
}
