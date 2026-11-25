import unittest

from norm import normalize


class TestNormlaize(unittest.TestCase):

    def test_normalize_close_max(self):
        result = normalize([20, 24, 25])
        self.assertEqual(result[-1], 1.0)

    def test_normalize_close_min(self):
        result = normalize([10, 20, 30])
        self.assertEqual(result[0], 0.0)


unittest.main()
