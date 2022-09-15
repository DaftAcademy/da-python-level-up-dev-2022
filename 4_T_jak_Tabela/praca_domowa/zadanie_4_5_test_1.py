import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/products/2/orders")
        self._response = requests.get(get_path)
        self._expected_response = {
            "orders": [
                {
                    "id": 10255,
                    "customer": "Richter Supermarkt",
                    "quantity": 20,
                    "total_price": 304.0,
                },
                {
                    "id": 10258,
                    "customer": "Ernst Handel",
                    "quantity": 50,
                    "total_price": 608.0,
                },
                {
                    "id": 10264,
                    "customer": "Folk och f HB",
                    "quantity": 35,
                    "total_price": 532.0,
                },
                {
                    "id": 10298,
                    "customer": "Hungry Owl All-Night Grocers",
                    "quantity": 40,
                    "total_price": 608.0,
                },
                {
                    "id": 10327,
                    "customer": "Folk och f HB",
                    "quantity": 25,
                    "total_price": 304.0,
                },
                {
                    "id": 10335,
                    "customer": "Hungry Owl All-Night Grocers",
                    "quantity": 7,
                    "total_price": 85.12,
                },
                {
                    "id": 10342,
                    "customer": "Frankenversand",
                    "quantity": 24,
                    "total_price": 291.84,
                },
                {
                    "id": 10393,
                    "customer": "Save-a-lot Markets",
                    "quantity": 25,
                    "total_price": 285.0,
                },
                {
                    "id": 10418,
                    "customer": "QUICK-Stop",
                    "quantity": 60,
                    "total_price": 912.0,
                },
                {
                    "id": 10435,
                    "customer": "Consolidated Holdings",
                    "quantity": 10,
                    "total_price": 152.0,
                },
                {
                    "id": 10440,
                    "customer": "Save-a-lot Markets",
                    "quantity": 45,
                    "total_price": 581.4,
                },
                {
                    "id": 10469,
                    "customer": "White Clover Markets",
                    "quantity": 40,
                    "total_price": 516.8,
                },
                {
                    "id": 10485,
                    "customer": "LINO-Delicateses",
                    "quantity": 20,
                    "total_price": 273.6,
                },
                {
                    "id": 10504,
                    "customer": "White Clover Markets",
                    "quantity": 12,
                    "total_price": 228.0,
                },
                {
                    "id": 10611,
                    "customer": "Wolski  Zajazd",
                    "quantity": 10,
                    "total_price": 190.0,
                },
                {
                    "id": 10622,
                    "customer": "Ricardo Adocicados",
                    "quantity": 20,
                    "total_price": 380.0,
                },
                {
                    "id": 10632,
                    "customer": "Die Wandernde Kuh",
                    "quantity": 30,
                    "total_price": 541.5,
                },
                {
                    "id": 10641,
                    "customer": "HILARION-Abastos",
                    "quantity": 50,
                    "total_price": 950.0,
                },
                {
                    "id": 10703,
                    "customer": "Folk och f HB",
                    "quantity": 5,
                    "total_price": 95.0,
                },
                {
                    "id": 10714,
                    "customer": "Save-a-lot Markets",
                    "quantity": 30,
                    "total_price": 427.5,
                },
                {
                    "id": 10722,
                    "customer": "Save-a-lot Markets",
                    "quantity": 3,
                    "total_price": 57.0,
                },
                {
                    "id": 10741,
                    "customer": "Around the Horn",
                    "quantity": 15,
                    "total_price": 228.0,
                },
                {
                    "id": 10766,
                    "customer": "Ottilies Kseladen",
                    "quantity": 40,
                    "total_price": 760.0,
                },
                {
                    "id": 10787,
                    "customer": "La maison d'Asie",
                    "quantity": 15,
                    "total_price": 270.75,
                },
                {
                    "id": 10792,
                    "customer": "Wolski  Zajazd",
                    "quantity": 10,
                    "total_price": 190.0,
                },
                {
                    "id": 10806,
                    "customer": "Victuailles en stock",
                    "quantity": 20,
                    "total_price": 285.0,
                },
                {
                    "id": 10813,
                    "customer": "Ricardo Adocicados",
                    "quantity": 12,
                    "total_price": 182.4,
                },
                {
                    "id": 10829,
                    "customer": "Island Trading",
                    "quantity": 10,
                    "total_price": 190.0,
                },
                {
                    "id": 10851,
                    "customer": "Ricardo Adocicados",
                    "quantity": 5,
                    "total_price": 90.25,
                },
                {
                    "id": 10852,
                    "customer": "Rattlesnake Canyon Grocery",
                    "quantity": 15,
                    "total_price": 285.0,
                },
                {
                    "id": 10856,
                    "customer": "Antonio Moreno Taquera",
                    "quantity": 20,
                    "total_price": 380.0,
                },
                {
                    "id": 10866,
                    "customer": "Berglunds snabbkp",
                    "quantity": 21,
                    "total_price": 299.25,
                },
                {
                    "id": 10885,
                    "customer": "Suprmes dlices",
                    "quantity": 20,
                    "total_price": 380.0,
                },
                {
                    "id": 10888,
                    "customer": "Godos Cocina Tpica",
                    "quantity": 20,
                    "total_price": 380.0,
                },
                {
                    "id": 10939,
                    "customer": "Magazzini Alimentari Riuniti",
                    "quantity": 10,
                    "total_price": 161.5,
                },
                {
                    "id": 10991,
                    "customer": "QUICK-Stop",
                    "quantity": 50,
                    "total_price": 760.0,
                },
                {
                    "id": 11021,
                    "customer": "QUICK-Stop",
                    "quantity": 11,
                    "total_price": 156.75,
                },
                {
                    "id": 11030,
                    "customer": "Save-a-lot Markets",
                    "quantity": 100,
                    "total_price": 1425.0,
                },
                {
                    "id": 11041,
                    "customer": "Chop-suey Chinese",
                    "quantity": 30,
                    "total_price": 456.0,
                },
                {
                    "id": 11049,
                    "customer": "Gourmet Lanchonetes",
                    "quantity": 10,
                    "total_price": 152.0,
                },
                {
                    "id": 11070,
                    "customer": "Lehmanns Marktstand",
                    "quantity": 20,
                    "total_price": 323.0,
                },
                {
                    "id": 11072,
                    "customer": "Ernst Handel",
                    "quantity": 8,
                    "total_price": 152.0,
                },
                {
                    "id": 11075,
                    "customer": "Richter Supermarkt",
                    "quantity": 10,
                    "total_price": 161.5,
                },
                {
                    "id": 11077,
                    "customer": "Rattlesnake Canyon Grocery",
                    "quantity": 24,
                    "total_price": 364.8,
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
