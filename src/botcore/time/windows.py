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


def friday_thursday_window(
    weeks_ago: int = 0,
    today: date | None = None,
) -> tuple[date, date]:
    """
    Return the most recently completed Friday-Thursday reporting window.

    weeks_ago=0 -> latest completed Fri-Thu week
    weeks_ago=1 -> prior Fri-Thu week
    """
    anchor = today or date.today()
    days_since_thursday = (anchor.weekday() - 3) % 7
    if days_since_thursday == 0:
        # If run on Thursday, that week is still in flight; use the previous one.
        days_since_thursday = 7
    last_thu = anchor - timedelta(days=days_since_thursday + (weeks_ago * 7))
    last_fri = last_thu - timedelta(days=6)
    return last_fri, last_thu


def friday_thursday_window_iso(
    weeks_ago: int = 0,
    today: date | None = None,
) -> tuple[str, str]:
    """ISO-string variant of `friday_thursday_window`."""
    start, end = friday_thursday_window(weeks_ago=weeks_ago, today=today)
    return start.isoformat(), end.isoformat()
