import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/categories")
        self._response = requests.get(get_path)
        self._expected_response = {
            "categories": [
                {"id": 1, "name": "Beverages"},
                {"id": 2, "name": "Condiments"},
                {"id": 3, "name": "Confections"},
                {"id": 4, "name": "Dairy Products"},
                {"id": 5, "name": "Grains/Cereals"},
                {"id": 6, "name": "Meat/Poultry"},
                {"id": 7, "name": "Produce"},
                {"id": 8, "name": "Seafood"},
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
