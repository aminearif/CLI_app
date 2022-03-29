import unittest
from main import print_date

class TestMain(unittest.TestCase) :

    def test_in_range(self):
        self.assertEqual(print_date("02-01-2022", "08-01-2022"))