import unittest

from my_code import mean, normalize


class TeatMean(unittest.TestCase):

    def test_eamn_values(self):
        self.assertEqual(mean([10, 20, 30]), 20.01)


unittest.main()
