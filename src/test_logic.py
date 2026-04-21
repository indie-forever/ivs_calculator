##
# @file test_logic.py
# @author Simona Studená (xstudes00)
# @brief Integration tests for the CalculatorController logic.
#

import unittest
from logic import CalculatorController

##
# @class TestMain
# @brief Test suite for validating calculator input and output.
#
class TestMain(unittest.TestCase):
    ##
    # @brief Setup before each test case.
    #
    def setUp(self):
        self.ctrl = CalculatorController()

    ##
    # @brief Test if typing numbers correctly updates the string display.
    #
    def test_writing_numbers(self):
        self.ctrl.handle_button("1")
        self.ctrl.handle_button("2")
        self.assertEqual(self.ctrl.get_display_text(), "12")

    ##
    # @brief Test if numbers starting with zeros are displayed correctly.
    #
    def test_writing_numbers_zero(self):
        self.ctrl.handle_button("0")
        self.ctrl.handle_button("5")
        self.assertEqual(self.ctrl.get_display_text(), "5")

    ##
    # @brief Test addition correctness and float string formatting.
    #
    def test_addition(self):
        self.ctrl.handle_button("5")
        self.ctrl.handle_button("+")
        self.ctrl.handle_button("3")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "8.0")
    ##
    # @brief Test substitution correctness and float string formatting.
    #
    def test_substitution(self):
        self.ctrl.handle_button("5")
        self.ctrl.handle_button("-")
        self.ctrl.handle_button("8")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "-3.0")

    ##
    # @brief Test multiplication correctness and float string formatting.
    #
    def test_multiplication(self):
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("*")
        self.ctrl.handle_button("3")
        self.ctrl.handle_button("=")
        # Expected "5.0" as a string
        self.assertEqual(self.ctrl.get_display_text(), "6.0")
    ##
    # @brief Test typing and calculating with decimal numbers.
    #
    def test_mul_decimal_input(self):
        self.ctrl.handle_button("2")
        self.ctrl.handle_button(".")
        self.ctrl.handle_button("5")
        self.ctrl.handle_button("*")
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("=")
        # Expected "5.0" as a string
        self.assertEqual(self.ctrl.get_display_text(), "5.0")

    ##
    # @brief Test multiplication by zero.
    #
    def test_multiplication_by_zero(self):
        self.ctrl.handle_button("5")
        self.ctrl.handle_button("*")
        self.ctrl.handle_button("0")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "0.0")

    ##
    # @brief Test division correctness and float string formatting.
    #
    def test_division(self):
        self.ctrl.handle_button("9")
        self.ctrl.handle_button("/")
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "4.5")

    ##
    # @brief Test division by zero returning a "Error" string.
    #
    def test_division_by_zero(self):
        self.ctrl.handle_button("15")
        self.ctrl.handle_button("/")
        self.ctrl.handle_button("0")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "Error")

    ##
    # @brief Test factorial correctness and float string formatting.
    #
    def test_factorial(self):
        self.ctrl.handle_button("5")
        self.ctrl.handle_button("!")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "120.0")

    ##
    # @brief Test logarithm of a base 10 correctness and float string formatting.
    #
    def test_logarithm(self):
        self.ctrl.handle_button("1")
        self.ctrl.handle_button("0")
        self.ctrl.handle_button("log")
        self.ctrl.handle_button("1")
        self.ctrl.handle_button("0")
        self.ctrl.handle_button("0")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "2.0")

    ##
    # @brief Test logarithm correctness and float string formatting.
    #
    def test_logarithm_dif_base(self):
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("log")
        self.ctrl.handle_button("8")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "3.0")

    ##
    # @brief Test power correctness and float string formatting.
    #
    def test_power(self):
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("^")
        self.ctrl.handle_button("3")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "8.0")
    
    ##
    # @brief Test the root operation correctness and float string formatting.
    #
    def test_root(self):
        self.ctrl.handle_button("9")
        self.ctrl.handle_button("root")
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "3.0")

    ##
    # @brief Test priotity of operands in an expression.
    #
    def test_priority(self):
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("+")
        self.ctrl.handle_button("3")
        self.ctrl.handle_button("*")
        self.ctrl.handle_button("4")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "14.0")

    ##
    # @brief Test parentheses changing the order of evaluation.
    #
    def test_brackets_and_priority(self):
        self.ctrl.handle_button("(")
        self.ctrl.handle_button("2")
        self.ctrl.handle_button("+")
        self.ctrl.handle_button("3")
        self.ctrl.handle_button(")")
        self.ctrl.handle_button("*")
        self.ctrl.handle_button("4")
        self.ctrl.handle_button("=")
        self.assertEqual(self.ctrl.get_display_text(), "20.0")

    if __name__ == '__main__':
        unittest.main()