import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/products/48/orders")
        self._response = requests.get(get_path)
        self._expected_response = {
            "orders": [
                {
                    "id": 10403,
                    "customer": "Ernst Handel",
                    "quantity": 70,
                    "total_price": 606.9,
                },
                {
                    "id": 10453,
                    "customer": "Around the Horn",
                    "quantity": 15,
                    "total_price": 137.7,
                },
                {
                    "id": 10507,
                    "customer": "Antonio Moreno Taquera",
                    "quantity": 15,
                    "total_price": 162.56,
                },
                {
                    "id": 10604,
                    "customer": "Furia Bacalhau e Frutos do Mar",
                    "quantity": 6,
                    "total_price": 68.85,
                },
                {
                    "id": 10704,
                    "customer": "Queen Cozinha",
                    "quantity": 24,
                    "total_price": 306.0,
                },
                {
                    "id": 10814,
                    "customer": "Victuailles en stock",
                    "quantity": 8,
                    "total_price": 86.7,
                },
            ]
        }

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_response(self):
        self.assertEqual(
            self._response.json(),
            self._expected_response,
        )


if __name__ == "__main__":
    unittest.main()
