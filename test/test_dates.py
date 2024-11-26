import unittest
from datetime import datetime, timedelta

from src.date_utils import parse_date


class TestParsePostDate(unittest.TestCase):
    def setUp(self):
        """Set up today's date for relative time tests."""
        self.today = datetime.now()

    def test_hours_ago(self):
        """Test parsing relative time in hours."""
        raw_date = "6 hours ago"
        expected_date = (self.today - timedelta(hours=6)).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

        raw_date = "21 hours ago"
        expected_date = (self.today - timedelta(hours=21)).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

    def test_yesterday(self):
        """Test parsing 'yesterday'."""
        raw_date = "Yesterday"
        expected_date = (self.today - timedelta(days=1)).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

    def test_days_ago(self):
        """Test parsing 'x days ago'."""
        raw_date = "3 days ago"
        expected_date = (self.today - timedelta(days=3)).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

    def test_specific_dates_recent_month(self):
        """Test parsing specific dates in the current or recent month."""
        raw_date = "November 19"
        expected_date = self.today.replace(month=11, day=19).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

        raw_date = "November 11"
        expected_date = self.today.replace(month=11, day=11).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

    def test_specific_dates_older_month(self):
        """Test parsing specific dates from older months."""
        raw_date = "October 31"
        expected_date = self.today.replace(year=self.today.year - 1 if self.today.month < 10 else self.today.year,
                                           month=10, day=31).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

        raw_date = "September 30"
        expected_date = self.today.replace(year=self.today.year - 1 if self.today.month < 9 else self.today.year,
                                           month=9, day=30).strftime("%Y-%m-%d")
        self.assertEqual(parse_date(raw_date), expected_date)

    def test_leap_year(self):
        """Testing dates with leap years."""
        # Test February 29 without a year (closest past)
        raw_date = "February 29"
        result = parse_date(raw_date)
        today = datetime.now()

        # Determine the closest past February 29
        year = today.year
        while True:
            try:
                closest_date = datetime(year, 2, 29)
                if closest_date <= today:
                    expected = closest_date.strftime("%Y-%m-%d")
                    break
                year -= 1
            except ValueError:
                year -= 1

        self.assertEqual(result, expected, f"Failed for raw_date: {raw_date}")

        # Test February 29 in a specific leap year
        raw_date = "Feb 29, 2020"
        result = parse_date(raw_date)
        expected = "2020-02-29"
        self.assertEqual(result, expected, f"Failed for raw_date: {raw_date}")

        # Test February 29 in a non-leap year (should return None)
        raw_date = "Feb 29, 2023"
        result = parse_date(raw_date)
        self.assertIsNone(result, f"Expected None for invalid leap year date: {raw_date}")


if __name__ == "__main__":
    unittest.main()
