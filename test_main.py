import unittest
from main import print_date

class TestMain(unittest.TestCase) :

    def test_in_range(self):
        dict = {1641078000: 500, 1641164400: 700, 1641250800: 1300, 1641337200: 2000, 1641423600: 3000, 1641510000: 3500, 1641596400: 4000}
        self.assertEqual( print_date("02-01-2022", "08-01-2022"), dict)

    # def test_not_in_range(self):
    #     self.assertEqual( print_date("27-03-2022", "27-04-2022"), "Date is not in range")

if __name__ == '__main__':
    unittest.main()
