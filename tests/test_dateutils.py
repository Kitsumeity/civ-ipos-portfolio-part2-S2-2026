import unittest
from src.date_controller import before_today, parse, format_date
import datetime


class TestDateController(unittest.TestCase):

    def test_parse_date_1(self):
        date = "12 10 2004"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_2(self):
        date = "Oct 12 2004"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_3(self):
        date = "12 Oct 2004"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_4(self):
        date = "2004 12 Oct"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_5(self):
        date = "2004 Oct 12"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_6(self):
        date = "2004 12 10"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_7(self):
        date = "12th 2004 Oct"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_8(self):
        date = "12th-2004-October"
        expected = datetime.date(2004, 10, 12)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_parse_date_9(self):
        date = "10 12 2004"
        expected = datetime.date(2004, 12, 10)
        result = parse(date)
        self.assertEqual(expected, result)

    def test_invalid_parse_date(self):
        date = "654 18 2004"
        result = parse(date)
        self.assertIsNone(result)

    def test_reformat_date(self):
        date = "12 10 2004"
        expected = "12 Oct 2004"
        result = format_date(date)
        self.assertEqual(expected, result)

    def test_invalid_reformat_date(self):
        date = "654 18 2004"
        result = format_date(date)
        self.assertIsNone(result)

    def test_before_today(self):
        date = "24 7 2001"
        today = datetime.date(2004, 10, 12)
        result = before_today(date, today_date=today)
        self.assertTrue(result)

    def test_after_today(self):
        date = "16 10 2026"
        today = datetime.date(2004, 10, 12)
        result = before_today(date, today_date=today)
        self.assertFalse(result)

    def test_before_today_invalid(self):
        date = "16 1d 2026"
        today = datetime.date(2004, 10, 12)
        result = before_today(date, today_date=today)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
