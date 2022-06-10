from distutils.log import error
import requests
import pprint
from product import Product
from processed_data import ProcessedData
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-url", "--url", help="Raw data URL")
parser.add_argument('unittest_args', nargs='*')

args = parser.parse_args()

def get_products():
    res = requests.get(
        args.url)
    if res.status_code == 200:
        products = res.json()['products']
    else:
        products = []
    return products

def process_products(products):
    """Returns ProcessedData class object with available_products, unique_brands, unique_products and prices properties"""
    available_products = []  # Not hidden and not deleted
    unique_brands = set()
    unique_products = set()
    prices = []
    for product in products:
        if not product['hidden'] and not product['deleted']:
            try:
                product['price'] = float(product['price'].strip('$'))
            except:
                print(error)
                continue
            available_product = Product(
                product['brand_name'], product['product_name'], product['price'])

            # Assuming a product is only available under the same brand
            if available_product.product_name not in unique_products:
                available_products.append(available_product)
                prices.append(product['price'])
            unique_brands.add(available_product.brand_name)
            unique_products.add(available_product.product_name)
    processed_data = ProcessedData(
        available_products, unique_brands, unique_products, prices)
    return processed_data


def main():
    products = get_products()
    processed_data = process_products(products)
    summary = processed_data.format_summary()
    pprint.pprint(summary)
    available_products = processed_data.sort_products()
    pprint.pprint(available_products)


if __name__ == "__main__":
    main()
