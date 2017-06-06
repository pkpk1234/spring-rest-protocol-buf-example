'''
    1. install protoc python: sudo pip install protorpc

    2. generate python proto stub: protoc -I spring-rest-proto-service/src/main/proto/ --python_out=python-protobuf-client spring-rest-proto-service/src/main/proto/*.proto

    3. import http and proto lib, send http request to service, and parse to string
'''
import Product_pb2
import urllib
if __name__ == '__main__':
    product = Product_pb2.Product()
    product_read = urllib.urlopen("http://localhost:8080/firstprod").read()

    product.ParseFromString(product_read)
    print product
