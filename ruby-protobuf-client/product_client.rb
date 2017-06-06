#!/usr/bin/env ruby
=begin
  1. require http, proto lib
  2. generate protobuf ruby client: protoc -I spring-rest-proto-service/src/main/proto/ --ruby_out=ruby-protobuf-client spring-rest-proto-service/src/main/proto/*.proto
  3. parse http response
=end
require 'net/http'
require 'uri'
require 'Product_pb'

uri = URI.parse('http://localhost:8080/firstprod')
body = Net::HTTP.get(uri)
puts Example::Product.parse(body)