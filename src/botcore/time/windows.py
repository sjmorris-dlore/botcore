"""Reporting window helpers shared across bots."""

from __future__ import annotations

from datetime import date, timedelta


def settled_week_window(weeks_ago: int = 0, today: date | None = None) -> tuple[date, date]:
    """
    Return reporting window using settled data: 8 days ago through 2 days ago.

    weeks_ago=0 gives the latest settled 7-day window.
    weeks_ago=1 shifts the entire window one week back.
    """
    anchor = today or date.today()
    end = anchor - timedelta(days=2 + (weeks_ago * 7))
    start = anchor - timedelta(days=8 + (weeks_ago * 7))
    return start, end


def settled_week_window_iso(
    weeks_ago: int = 0,
    today: date | None = None,
) -> tuple[str, str]:
    """ISO-string variant of `settled_week_window`."""
    start, end = settled_week_window(weeks_ago=weeks_ago, today=today)
    return start.isoformat(), end.isoformat()

