"""
Unit Test
This is a sample of a unit test, check the README.md
"""
import unittest
from my_code import MyBasicMath


class TestBasicMath(unittest.TestCase):
    my_math = None

    @classmethod
    def tearDownClass(cls):
        del cls.my_math

    @classmethod
    def setUpClass(cls):
        cls.my_math = MyBasicMath()

    def setUp(self):
        self._my_math = MyBasicMath()

    def tearDown(self):
        del self._my_math

    def test_sum(self):
        self.assertEqual(self.my_math.add(2, 4), 6)

    def test_mul(self):
        self.assertEqual(self.my_math.mul(6, 4), 24)

    def test_sub(self):
        self.assertEqual(self.my_math.sub(4, -9), 13)

    @unittest.expectedFailure
    def test_sub_to_fail(self):
        self.assertEqual(self.my_math.sub(3, 5), 15)

    def test_div(self):
        self.assertEqual(self.my_math.div(40, 4), 10)

    @unittest.expectedFailure
    def test_div_to_fail(self):
        self.assertIsNotNone(self.my_math.div(4, 0))
