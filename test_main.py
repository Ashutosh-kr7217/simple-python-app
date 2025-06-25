import unittest
from main import greet


class TestGreet(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Ashutosh"), "Hello, Ashutosh!")


if __name__ == "__main__":
    unittest.main()
