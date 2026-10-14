import unittest
from pathlib import Path
from summarize_logs import summarize

class SummaryTests(unittest.TestCase):
    def test_synthetic_fixture_counts(self):
        lines = Path(__file__).with_name("sample-auth.log").read_text().splitlines()
        outcomes, users, malformed = summarize(lines)
        self.assertEqual(dict(outcomes), {"failure": 4, "success": 2})
        self.assertEqual(dict(users), {"demo-a": 2, "demo-b": 1, "demo-c": 1})
        self.assertEqual(malformed, 0)

    def test_comments_and_empty_input(self):
        outcomes, users, malformed = summarize(["", "# comment"])
        self.assertEqual(sum(outcomes.values()), 0)
        self.assertFalse(users)
        self.assertEqual(malformed, 0)

    def test_bad_or_unknown_records_are_counted(self):
        outcomes, users, malformed = summarize([
            "invalid record", "time user=a result=unknown ip=192.0.2.1",
            "time user=a result=success ip=192.0.2.1"])
        self.assertEqual(malformed, 2)
        self.assertEqual(outcomes["success"], 1)
        self.assertFalse(users)

if __name__ == "__main__":
    unittest.main()
