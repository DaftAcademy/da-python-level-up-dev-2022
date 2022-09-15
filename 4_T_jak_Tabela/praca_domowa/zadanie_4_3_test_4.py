import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(
            AppClass.APP_URL, "/employees?limit=3&offset=3&order=first_name"
        )
        self._response = requests.get(get_path)
        self._expected_response = {
            "employees": [
                {
                    "id": 8,
                    "last_name": "Callahan",
                    "first_name": "Laura",
                    "city": "Seattle",
                },
                {
                    "id": 4,
                    "last_name": "Peacock",
                    "first_name": "Margaret",
                    "city": "Redmond",
                },
                {
                    "id": 6,
                    "last_name": "Suyama",
                    "first_name": "Michael",
                    "city": "London",
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
