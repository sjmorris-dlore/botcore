import unittest
from datetime import datetime, timedelta, timezone

from botcore.metrics.maturity import engagement_maturity, projected_score


class MaturityTests(unittest.TestCase):
    def test_maturity_curve_outputs(self):
        now = datetime(2026, 3, 2, 12, 0, 0, tzinfo=timezone.utc)

        m_1h = engagement_maturity((now - timedelta(hours=1)).isoformat(), now=now)
        m_6h = engagement_maturity((now - timedelta(hours=6)).isoformat(), now=now)
        m_24h = engagement_maturity((now - timedelta(hours=24)).isoformat(), now=now)

        # Lock behavior to existing fitted coefficients used in igbot/growthbot.
        self.assertAlmostEqual(m_1h, 0.222678, places=5)
        self.assertAlmostEqual(m_6h, 0.480238, places=5)
        self.assertAlmostEqual(m_24h, 0.745800, places=5)

    def test_projected_score(self):
        now = datetime(2026, 3, 2, 12, 0, 0, tzinfo=timezone.utc)
        published = (now - timedelta(hours=6)).isoformat()
        proj = projected_score(100.0, published, now=now)
        self.assertAlmostEqual(proj, 208.23, places=2)

    def test_invalid_timestamp_falls_back(self):
        self.assertEqual(engagement_maturity("not-a-date"), 1.0)
        self.assertEqual(projected_score(12.34, "not-a-date"), 12.34)


if __name__ == "__main__":
    unittest.main()
