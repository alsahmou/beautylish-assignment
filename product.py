class Product:
    def __init__(self, brand_name, product_name, price):
        self.brand_name = brand_name
        self.product_name = product_name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        return self.brand_name == other.brand_name \
            and self.product_name == other.product_name and \
            self.price == self.price

    def __ne__(self, other):
        return self.brand_name != other.brand_name \
            and self.product_name != other.product_name and \
            self.price != self.price
