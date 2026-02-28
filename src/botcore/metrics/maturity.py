"""Engagement maturity model and projection helper."""

from __future__ import annotations

import math
from datetime import datetime, timezone


MATURITY_LAMBDA = 0.2519
MATURITY_ALPHA = 0.5328
MIN_MATURITY = 0.20


def engagement_maturity(
    published_at_iso: str,
    now: datetime | None = None,
) -> float:
    """
    Fraction of final engagement expected at current age.

    Model:
      maturity = 1 - exp(-0.2519 * hours^0.5328)
    """
    try:
        published = datetime.fromisoformat(published_at_iso.replace("Z", "+00:00"))
        current = now or datetime.now(timezone.utc)
        hours = max((current - published).total_seconds() / 3600.0, 0.5)
        maturity = 1.0 - math.exp(-MATURITY_LAMBDA * (hours ** MATURITY_ALPHA))
        return max(maturity, MIN_MATURITY)
    except Exception:
        return 1.0


def projected_score(
    raw_score: float,
    published_at_iso: str,
    now: datetime | None = None,
    ndigits: int = 2,
) -> float:
    """Age-normalized performance score."""
    m = engagement_maturity(published_at_iso=published_at_iso, now=now)
    return round(raw_score / m, ndigits)

