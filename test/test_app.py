import unittest
from flask import Flask

class TestPostAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app.test_clinet()

    def test_find_pairs(self):
        data = {"numbers": [1, 2, 3, 4, 5],"target": 6}
        response = self.app.post('http://127.0.0.1:5000/find-pairs', json=data)

        self.assertEqual(response.status_code == 201)

