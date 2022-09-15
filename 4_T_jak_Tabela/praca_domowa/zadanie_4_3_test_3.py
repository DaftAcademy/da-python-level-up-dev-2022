import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(
            AppClass.APP_URL, "/employees?limit=4&offset=2&order=city"
        )
        self._response = requests.get(get_path)
        self._expected_response = {
            "employees": [
                {
                    "id": 6,
                    "last_name": "Suyama",
                    "first_name": "Michael",
                    "city": "London",
                },
                {
                    "id": 7,
                    "last_name": "King",
                    "first_name": "Robert",
                    "city": "London",
                },
                {
                    "id": 9,
                    "last_name": "Dodsworth",
                    "first_name": "Anne",
                    "city": "London",
                },
                {
                    "id": 4,
                    "last_name": "Peacock",
                    "first_name": "Margaret",
                    "city": "Redmond",
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
