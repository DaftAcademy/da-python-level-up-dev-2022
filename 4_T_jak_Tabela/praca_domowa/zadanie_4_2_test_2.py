import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/products/4")
        self._response = requests.get(get_path)
        self._expected_response = {"id": 4, "name": "Chef Anton's Cajun Seasoning"}

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 200)

    def test_response(self):
        self.assertEqual(
            self._response.json(),
            self._expected_response,
        )


if __name__ == "__main__":
    unittest.main()
