# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Products.proto

require 'google/protobuf'

require 'Product_pb'
Google::Protobuf::DescriptorPool.generated_pool.build do
  add_message "example.Products" do
    repeated :products, :message, 1, "example.Product"
  end
end

module Example
  Products = Google::Protobuf::DescriptorPool.generated_pool.lookup("example.Products").msgclass
end