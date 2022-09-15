import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        get_path = urllib.parse.urljoin(AppClass.APP_URL, "/employees?order=invalid")
        self._response = requests.get(get_path)

    def test_status_code(self):
        self.assertEqual(self._response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
