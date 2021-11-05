import unittest
from main import min

class MyTestCase(unittest.TestCase):
    def test_min(self):
        self.assertEqual(min(1,[1,-3,6],0),-3)