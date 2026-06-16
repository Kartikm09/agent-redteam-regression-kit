import unittest

from redteam_kit.scenarios import classify_response


class ScenarioTests(unittest.TestCase):
    def test_classify_response_flags_permission_overreach(self):
        flags = classify_response("Grant access and make it public.")

        self.assertIn("permission-overreach", flags)


if __name__ == "__main__":
    unittest.main()
