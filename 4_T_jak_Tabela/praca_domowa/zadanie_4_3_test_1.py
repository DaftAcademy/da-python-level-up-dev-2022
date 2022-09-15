import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/employees?limit=3")
        self._response = requests.get(get_path)
        self._expected_response = {
            "employees": [
                {
                    "id": 1,
                    "last_name": "Davolio",
                    "first_name": "Nancy",
                    "city": "Seattle",
                },
                {
                    "id": 2,
                    "last_name": "Fuller",
                    "first_name": "Andrew",
                    "city": "Tacoma",
                },
                {
                    "id": 3,
                    "last_name": "Leverling",
                    "first_name": "Janet",
                    "city": "Kirkland",
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
