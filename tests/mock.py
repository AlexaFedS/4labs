from ..builder import *
from unittest import TestCase
from unittest.mock import patch

class Testgate(TestCase):
    @patch('builder.check_sum', return_value=12132)
    def test_sum_cost(self, x):
        self.assertEqual(check_sum(0), 12132)