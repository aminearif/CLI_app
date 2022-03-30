import unittest
import functions
import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL= os.getenv('USER_BASE_URL')

class TestMain(unittest.TestCase) :

    # unit test for dates in range
    def test_in_range(self):
        self.assertTrue(functions.filter_date("02-01-2022", "08-01-2022"))

    # unit test for dates not in range
    def test_not_in_range(self):
        self.assertFalse(functions.filter_date("02-01-2023", "08-01-2023"))

    # network test for request userbase
    def test_get_user_activity(self):
        response = requests.get(URL)
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
