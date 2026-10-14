import unittest
from src.date_controller import DateController


class TestDateController(unittest.TestCase):

    def test_reformat_date(self):
        date = "12 10 2004"

        expected = "12 Oct 2004"
        result = DateController.format_date(date)

        self.assertEqual(expected, result)



if __name__ == "__main__":
    unittest.main()