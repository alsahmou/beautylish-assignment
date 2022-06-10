import unittest
from main import process_products
from processed_data import ProcessedData
from product import Product


class TestMain(unittest.TestCase):

    def test_process_products(self):
        raw_data = [{"deleted": False, "brand_name": "Acme",
                     "product_name": "widget", "price": "$99.85", "hidden": False, "id": 1},
                    {"deleted": False, "brand_name": "Hooli",
                     "product_name": "Nucleus", "price": "$10.00", "hidden": False, "id": 2}]
        expected_processed_data = ProcessedData(
            [Product("Acme", "widget", 99.85),
             Product("Hooli", "Nucleus", 10.00)],
            {"Acme", "Hooli"}, {"widget", "Nucleus"}, [99.85, 10.00])

        self.assertEqual(process_products(raw_data), expected_processed_data)

    def test_process_products_deleted(self):
        raw_data = [{"deleted": True, "brand_name": "Acme",
                     "product_name": "widget", "price": "$99.85", "hidden": False, "id": 1}]
        expected_processed_data = ProcessedData(
            [], set(), set(), [])

        self.assertEqual(process_products(raw_data), expected_processed_data)

    def test_process_products_hidden(self):
        raw_data = [{"deleted": False, "brand_name": "Acme",
                     "product_name": "widget", "price": "$99.85", "hidden": True, "id": 1}]
        expected_processed_data = ProcessedData(
            [], set(), set(), [])

        self.assertEqual(process_products(raw_data), expected_processed_data)

    def test_process_products_deleted_and_hidden(self):
        raw_data = [{"deleted": True, "brand_name": "Acme",
                     "product_name": "widget", "price": "$99.85", "hidden": True, "id": 1}]
        expected_processed_data = ProcessedData(
            [], set(), set(), [])

        self.assertEqual(process_products(raw_data), expected_processed_data)
