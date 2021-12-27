import unittest
import sys, os

sys.path.append(os.getcwd())
from ..builder import *

class Testgate(unittest.TestCase):

    def test_gate(self):
        self.assertEqual(check_gate("MoscowPerm"), 1)

if __name__ == "__main__":
    unittest.main()