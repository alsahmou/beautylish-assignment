import pprint
import statistics

class ProcessedData():
    def __init__(self, available_products, unique_brands, unique_products, prices):
        self.available_products = available_products
        self.unique_brands = unique_brands
        self.unique_products = unique_products
        self.prices = prices

    def __eq__(self, other):
        if not isinstance(other, ProcessedData):
            return NotImplemented

        return self.available_products == other.available_products \
            and self.unique_brands == other.unique_brands and \
            self.unique_products == self.unique_products and self.prices == other.prices

    def __ne__(self, other):
        return self.available_products != other.available_products \
            and self.unique_brands != other.unique_brands and \
            self.unique_products != self.unique_products and self.prices != other.prices

    def format_summary(self):
        unique_brands = self.unique_brands
        unique_products = self.unique_products
        prices = self.prices
        average_price = statistics.mean(prices)
        average_price = "{:.2f}".format(round(average_price, 2))
        summary = {
            'Unique Brands': unique_brands,
            'Unique Products': unique_products,
            'Average Price': average_price
        }
        return summary

    def sort_products(self):
        return sorted(
            self.available_products, key=lambda x: (x.price, x.product_name))
