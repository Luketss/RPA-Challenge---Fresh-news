import unittest
import datetime
from util import set_month_range


class TestGenerateDateRange(unittest.TestCase):
    def test_today_date_range(self):
        start, end = set_month_range(1)
        today = datetime.date.today()
        expected_start = today.replace(day=1).strftime("%m/%d/%Y")
        expected_end = today.strftime("%m/%d/%Y")
        self.assertEqual(start, expected_start)
        self.assertEqual(end, expected_end)

    def test_one_month_ago_date_range(self):
        start, end = set_month_range(2)
        today = datetime.date.today()
        expected_start = (
            (today - datetime.timedelta(days=30)).replace(day=1).strftime("%m/%d/%Y")
        )
        expected_end = today.strftime("%m/%d/%Y")
        self.assertEqual(start, expected_start)
        self.assertEqual(end, expected_end)

    def test_six_months_ago_date_range(self):
        start, end = set_month_range(7)
        today = datetime.date.today()
        expected_start = (
            (today - datetime.timedelta(days=180)).replace(day=1).strftime("%m/%d/%Y")
        )
        expected_end = today.strftime("%m/%d/%Y")
        self.assertEqual(start, expected_start)
        self.assertEqual(end, expected_end)


if __name__ == "__main__":
    unittest.main()
