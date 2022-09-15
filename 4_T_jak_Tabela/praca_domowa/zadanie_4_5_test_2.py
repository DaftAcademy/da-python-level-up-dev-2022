import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/products/10/orders")
        self._response = requests.get(get_path)
        self._expected_response = {
            "orders": [
                {
                    "id": 10273,
                    "customer": "QUICK-Stop",
                    "quantity": 24,
                    "total_price": 565.44,
                },
                {
                    "id": 10276,
                    "customer": "Tortuga Restaurante",
                    "quantity": 15,
                    "total_price": 372.0,
                },
                {
                    "id": 10357,
                    "customer": "LILA-Supermercado",
                    "quantity": 30,
                    "total_price": 595.2,
                },
                {
                    "id": 10389,
                    "customer": "Bottom-Dollar Markets",
                    "quantity": 16,
                    "total_price": 396.8,
                },
                {
                    "id": 10449,
                    "customer": "Blondesddsl pre et fils",
                    "quantity": 14,
                    "total_price": 347.2,
                },
                {
                    "id": 10450,
                    "customer": "Victuailles en stock",
                    "quantity": 20,
                    "total_price": 396.8,
                },
                {
                    "id": 10478,
                    "customer": "Victuailles en stock",
                    "quantity": 20,
                    "total_price": 471.2,
                },
                {
                    "id": 10519,
                    "customer": "Chop-suey Chinese",
                    "quantity": 16,
                    "total_price": 471.2,
                },
                {
                    "id": 10524,
                    "customer": "Berglunds snabbkp",
                    "quantity": 2,
                    "total_price": 62.0,
                },
                {
                    "id": 10568,
                    "customer": "Galera del gastrnomo",
                    "quantity": 5,
                    "total_price": 155.0,
                },
                {
                    "id": 10609,
                    "customer": "Du monde entier",
                    "quantity": 10,
                    "total_price": 310.0,
                },
                {
                    "id": 10612,
                    "customer": "Save-a-lot Markets",
                    "quantity": 70,
                    "total_price": 2170.0,
                },
                {
                    "id": 10646,
                    "customer": "Hungry Owl All-Night Grocers",
                    "quantity": 18,
                    "total_price": 418.5,
                },
                {
                    "id": 10664,
                    "customer": "Furia Bacalhau e Frutos do Mar",
                    "quantity": 24,
                    "total_price": 632.4,
                },
                {
                    "id": 10676,
                    "customer": "Tortuga Restaurante",
                    "quantity": 2,
                    "total_price": 62.0,
                },
                {
                    "id": 10685,
                    "customer": "Gourmet Lanchonetes",
                    "quantity": 20,
                    "total_price": 620.0,
                },
                {
                    "id": 10688,
                    "customer": "Vaffeljernet",
                    "quantity": 18,
                    "total_price": 502.2,
                },
                {
                    "id": 10713,
                    "customer": "Save-a-lot Markets",
                    "quantity": 18,
                    "total_price": 558.0,
                },
                {
                    "id": 10715,
                    "customer": "Bon app'",
                    "quantity": 21,
                    "total_price": 651.0,
                },
                {
                    "id": 10724,
                    "customer": "Mre Paillarde",
                    "quantity": 16,
                    "total_price": 496.0,
                },
                {
                    "id": 10775,
                    "customer": "The Cracker Box",
                    "quantity": 6,
                    "total_price": 186.0,
                },
                {
                    "id": 10785,
                    "customer": "GROSELLA-Restaurante",
                    "quantity": 10,
                    "total_price": 310.0,
                },
                {
                    "id": 10804,
                    "customer": "Seven Seas Imports",
                    "quantity": 36,
                    "total_price": 1116.0,
                },
                {
                    "id": 10827,
                    "customer": "Bon app'",
                    "quantity": 15,
                    "total_price": 465.0,
                },
                {
                    "id": 10841,
                    "customer": "Suprmes dlices",
                    "quantity": 16,
                    "total_price": 496.0,
                },
                {
                    "id": 10854,
                    "customer": "Ernst Handel",
                    "quantity": 100,
                    "total_price": 2635.0,
                },
                {
                    "id": 10874,
                    "customer": "Godos Cocina Tpica",
                    "quantity": 10,
                    "total_price": 310.0,
                },
                {
                    "id": 10886,
                    "customer": "Hanari Carnes",
                    "quantity": 70,
                    "total_price": 2170.0,
                },
                {
                    "id": 10924,
                    "customer": "Berglunds snabbkp",
                    "quantity": 20,
                    "total_price": 558.0,
                },
                {
                    "id": 10946,
                    "customer": "Vaffeljernet",
                    "quantity": 25,
                    "total_price": 775.0,
                },
                {
                    "id": 10949,
                    "customer": "Bottom-Dollar Markets",
                    "quantity": 30,
                    "total_price": 930.0,
                },
                {
                    "id": 11020,
                    "customer": "Ottilies Kseladen",
                    "quantity": 24,
                    "total_price": 632.4,
                },
                {
                    "id": 11077,
                    "customer": "Rattlesnake Canyon Grocery",
                    "quantity": 1,
                    "total_price": 31.0,
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
