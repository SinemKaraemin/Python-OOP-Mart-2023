from .product import Product


class ProductRepository:
    def __init__(self):
        self.products = []  # All products

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name: str):
        self.products.remove(product_name)

    def __repr__(self):
        return '\n'.join([f'{p}: {p.quantity}' for p in self.products])
