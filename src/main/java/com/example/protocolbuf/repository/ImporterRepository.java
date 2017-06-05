package com.example.protocolbuf.repository;

import com.example.protocolbuf.store.Importer;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Created by pkpk1234 on 2017/6/3.
 */
@Repository
public interface ImporterRepository extends JpaRepository<Importer, Long> {
}
