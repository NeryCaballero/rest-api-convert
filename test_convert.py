import unittest
from convert import app


class TestApi(unittest.TestCase):
    def test_get_ascii_1(self):
        with app.test_client() as client:
            json_body = ["A", "h", "H", "x"]
            result = client.post('/convert', json=json_body)  # <class 'bytes'>
            expected_response = b'[650,0,0,0]\n'
            self.assertEqual(expected_response, result.data)
            self.assertEqual(result.status_code, 200)

    def test_get_ascii_2(self):
        with app.test_client() as client:
            json_body = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "p", "y"]
            result = client.post('/convert', json=json_body)  # <class 'bytes'>
            expected_response = b'[970,980,990,1000,1010,1020,1030,0,0,0,0]\n'
            self.assertEqual(expected_response, result.data)
            self.assertEqual(result.status_code, 200)

    def test_get_ascii_3(self):
        with app.test_client() as client:
            json_body = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "M", "Z"]
            result = client.post('/convert', json=json_body)  # <class 'bytes'>
            expected_response = b'[650,660,670,680,690,700,710,0,0,0,0]\n'
            self.assertEqual(expected_response, result.data)
            self.assertEqual(result.status_code, 200)
