import unittest
from src.date_controller import DateController
import datetime


class TestDateController(unittest.TestCase):

    def test_parse_date_1(self):
        date = "12 10 2004"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_2(self):
        date = "Oct 12 2004"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_3(self):
        date = "12 Oct 2004"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_4(self):
        date = "2004 12 Oct"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_5(self):
        date = "2004 Oct 12"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_6(self):
        date = "2004 12 10"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_7(self):
        date = "12th 2004 Oct"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_8(self):
        date = "12th-2004-October"
        expected = datetime.date(2004, 10, 12)
        result = DateController.parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_9(self):
        date = "10 12 2004"
        expected = datetime.date(2004, 12, 10)
        result = DateController.parse(date)
        self.assertEqual(expected, result)



    def test_invalid_parse_date(self):
        date = "654 18 2004"
        result = DateController.parse(date)
        self.assertIsNone(result)

    def test_reformat_date(self):
        date = "12 10 2004"
        expected = "12 Oct 2004"
        result = DateController.format_date(date)
        self.assertEqual(expected, result)

    def test_invalid_reformat_date(self):
        date = "654 18 2004"
        result = DateController.format_date(date)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()