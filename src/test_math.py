import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from math_lib import MathLib

class TestMathBasic(unittest.TestCase):

    def test_add(self):
        self.assertEqual(MathLib.add(2, 2), 4)
        self.assertEqual(MathLib.add(-1, -1), -2)
    
    def test_sub(self):
        self.assertEqual(MathLib.sub(10, 5), 5)
        self.assertEqual(MathLib.sub(0, 5), -5)

    def test_mul(self):
        self.assertEqual(MathLib.mul(3, 3), 9)
        self.assertEqual(MathLib.mul(5, 0), 0)
        self.assertEqual(MathLib.mul(-2, 3), -6)

    def test_div(self):
        self.assertEqual(MathLib.div(10, 2), 5)
        self.assertIsNone(MathLib.div(10,0))

if __name__ == '__main__':
    unittest.main()