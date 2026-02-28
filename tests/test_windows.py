import unittest
from datetime import date

from botcore.time.windows import (
    friday_thursday_time_window,
    friday_thursday_time_window_iso,
    settled_week_time_window,
    settled_week_time_window_iso,
)


class SettledWeekWindowTests(unittest.TestCase):
    def test_default_window_for_monday_anchor(self):
        # Matches existing bot behavior:
        # Mon 2026-03-02 -> 2026-02-22 to 2026-02-28
        start, end = settled_week_time_window(today=date(2026, 3, 2))
        self.assertEqual(start, date(2026, 2, 22))
        self.assertEqual(end, date(2026, 2, 28))

    def test_weeks_ago_shift(self):
        this_start, this_end = settled_week_time_window(today=date(2026, 3, 2), weeks_ago=0)
        prev_start, prev_end = settled_week_time_window(today=date(2026, 3, 2), weeks_ago=1)
        self.assertEqual((this_start - prev_start).days, 7)
        self.assertEqual((this_end - prev_end).days, 7)

    def test_iso_variant(self):
        start, end = settled_week_time_window_iso(today=date(2026, 3, 2))
        self.assertEqual(start, "2026-02-22")
        self.assertEqual(end, "2026-02-28")


class FridayThursdayWindowTests(unittest.TestCase):
    def test_default_window_for_monday_anchor(self):
        # Mon 2026-03-02 -> Fri 2026-02-20 to Thu 2026-02-26
        start, end = friday_thursday_time_window(today=date(2026, 3, 2))
        self.assertEqual(start, date(2026, 2, 20))
        self.assertEqual(end, date(2026, 2, 26))

    def test_on_thursday_uses_prior_complete_week(self):
        # Thu 2026-02-26 should still resolve to prior completed Fri-Thu.
        start, end = friday_thursday_time_window(today=date(2026, 2, 26))
        self.assertEqual(start, date(2026, 2, 13))
        self.assertEqual(end, date(2026, 2, 19))

    def test_iso_variant(self):
        start, end = friday_thursday_time_window_iso(today=date(2026, 3, 2))
        self.assertEqual(start, "2026-02-20")
        self.assertEqual(end, "2026-02-26")


if __name__ == "__main__":
    unittest.main()
