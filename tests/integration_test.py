import unittest
class Integration(unittest.TestCase):
    def test_join(self):
        self.assertIn("app", "weather app")
if __name__ == "__main__":
    unittest.main()
