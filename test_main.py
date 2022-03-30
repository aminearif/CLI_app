import unittest
import functions

class TestMain(unittest.TestCase) :

    # unit test for dates in range
    def test_in_range(self):
        self.assertTrue(functions.filter_date("02-01-2022", "08-01-2022"))

    # unit test for dates not in range
    def test_not_in_range(self):
        self.assertFalse(functions.filter_date("02-01-2023", "08-01-2023"))

if __name__ == '__main__':
    unittest.main()
