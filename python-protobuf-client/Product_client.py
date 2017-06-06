import Product_pb2
import urllib
if __name__ == '__main__':
    product = Product_pb2.Product()
    product_read = urllib.urlopen("http://localhost:8080/firstprod").read()

    product.ParseFromString(product_read)
    print product
