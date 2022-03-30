import unittest
import requests

class TestRequest(unittest.TestCase) :

    def test_get_locations_for_us_90210_check_status_code_equals_200(self):
        response = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
