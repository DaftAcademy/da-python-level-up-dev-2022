import unittest
import urllib.parse

import requests

from file import AppClass


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        self.input_data = {"name": "Test NewCategory"}
        self.update_data = {"name": "Test Another NewCategory"}

    def test_cud_flow(self):
        post_path = urllib.parse.urljoin(AppClass.APP_URL, "/categories")
        post_response = requests.post(post_path, json=self.input_data)
        post_response_json = post_response.json()
        self.assertEqual(post_response.status_code, 201)
        self.assertEqual(post_response_json["name"], self.input_data["name"])
        self.assertTrue(post_response_json["id"])

        index_path = urllib.parse.urljoin(AppClass.APP_URL, f"/categories")

        get_path = urllib.parse.urljoin(
            AppClass.APP_URL, f"/categories/{post_response_json['id']}"
        )

        index_response = requests.get(index_path)
        index_response_json = index_response.json()
        last_record = index_response_json["categories"][-1]
        self.assertEqual(last_record["name"], self.input_data["name"])
        self.assertEqual(last_record["id"], post_response_json["id"])

        put_response = requests.put(get_path, json=self.update_data)
        put_response_json = put_response.json()
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response_json["id"], post_response_json["id"])
        self.assertEqual(put_response_json["name"], self.update_data["name"])

        index_response = requests.get(index_path)
        index_response_json = index_response.json()
        last_record = index_response_json["categories"][-1]
        self.assertEqual(last_record["name"], self.update_data["name"])
        self.assertEqual(last_record["id"], post_response_json["id"])

        delete_response = requests.delete(get_path)
        delete_response_json = delete_response.json()
        self.assertEqual(delete_response.status_code, 200)
        self.assertEqual(delete_response_json, {"deleted": 1})

        delete_response = requests.delete(get_path)
        delete_response_json = delete_response.json()
        self.assertEqual(delete_response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
