##
# @file test_math.py
# @author Simona Studená (xstudes00)
# @brief Unit tests for the mathematical library MathLib.
#

import unittest
from math_lib import MathLib

##
# @class TestMathBasic
# @brief Test suite for validating mathematical functions.
#
class TestMathBasic(unittest.TestCase):

    ##
    # @brief Test the addition operation with positive and negative numbers.
    #
    def test_add(self):
        self.assertEqual(MathLib.add(2, 2), 4)
        self.assertEqual(MathLib.add(-1, -1), -2)

    ##
    # @brief Test the subtraction operation with positive and negative numbers.
    #
    def test_sub(self):
        self.assertEqual(MathLib.sub(10, 5), 5)
        self.assertEqual(MathLib.sub(0, 5), -5)

    ##
    # @brief Test the multiplication operation including zero and negative results.
    #
    def test_mul(self):
        self.assertEqual(MathLib.mul(3, 3), 9)
        self.assertEqual(MathLib.mul(5, 0), 0)
        self.assertEqual(MathLib.mul(-2, 3), -6)

    ##
    # @brief Test the division operation with positive nad negative numbers.
    #
    def test_div(self):
        self.assertEqual(MathLib.div(10, 2), 5)
        self.assertEqual(MathLib.div(5, 2), 2.5)
        self.assertAlmostEqual(MathLib.div(10, 3), 3.3333333)

    ##
    # @brief Test the factorial operation including edge cases and invalid inputs.
    #
    def test_factorial(self):
        self.assertEqual(MathLib.factorial(0), 1)
        self.assertEqual(MathLib.factorial(1), 1)
        self.assertEqual(MathLib.factorial(5), 120)
        self.assertEqual(MathLib.factorial(10), 3628800)
        #Invalid inputs should assert None.
        self.assertIsNone(MathLib.factorial(-1))
        self.assertIsNone(MathLib.factorial(6.7))

    ##
    # @brief Test the power operation with various exponents including zero and negative values.
    #
    def test_pow(self):
        self.assertEqual(MathLib.pow(2, 3), 8)
        self.assertEqual(MathLib.pow(15, 2), 225)
        # Test negative bases.
        self.assertEqual(MathLib.pow(-2, 4), 16)
        self.assertEqual(MathLib.pow(-3, 3), -27)
        # Test zero exponent
        self.assertEqual(MathLib.pow(15, 0), 1)
        self.assertEqual(MathLib.pow(-5, 0), 1)
        # Test negative exponent.
        self.assertEqual(MathLib.pow(2, -1), 0.5)
        self.assertEqual(MathLib.pow(10, -2), 0.01)
        # Invalid input for this library's specific implementation
        self.assertIsNone(MathLib.pow(4, 0.5))

    ##
    # @brief Test the root operation using almost equal for float precision.
    #
    def test_root(self):
        self.assertAlmostEqual(MathLib.root(9, 2), 3.0)
        self.assertAlmostEqual(MathLib.root(27, 3), 3.0)
        self.assertAlmostEqual(MathLib.root(0, 2), 0.0)
        # Invalid inputs should return None.
        self.assertIsNone(MathLib.root(-4, 2))
        self.assertIsNone(MathLib.root(15, 0))

    ##
    # @brief Test the logarithm operation with different bases and invalid inputs.
    #
    def test_log(self):
        self.assertAlmostEqual(MathLib.log(10, 100), 2.0)
        self.assertAlmostEqual(MathLib.log(2, 8), 3.0)
        self.assertAlmostEqual(MathLib.log(5, 25), 2.0)
        # Invalid inputs should return None.
        self.assertIsNone(MathLib.log(15, -5))
        self.assertIsNone(MathLib.log(15, 0))
        self.assertIsNone(MathLib.log(1, 15))
        self.assertIsNone(MathLib.log(-2, 15))       
    
if __name__ == '__main__':
    unittest.main()