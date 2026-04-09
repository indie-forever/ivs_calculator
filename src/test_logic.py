import unittest
from logic import CalculatorController

class TestMain(unittest.TestCase):
    def test_writing_numbers(self):
        ctrl = CalculatorController()
        ctrl.handle_button("1")
        ctrl.handle_button("2")
        self.assertEqual(ctrl.get_display_text(), "12")

    def test_writing_numbers_zero(self):
        ctrl = CalculatorController()
        ctrl.handle_button("0")
        ctrl.handle_button("5")
        self.assertEqual(ctrl.get_display_text(), "5")

    def test_addition(self):
        ctrl = CalculatorController()
        ctrl.handle_button("5")
        ctrl.handle_button("+")
        ctrl.handle_button("3")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "8.0")

    def test_substitution(self):
        ctrl = CalculatorController()
        ctrl.handle_button("5")
        ctrl.handle_button("-")
        ctrl.handle_button("8")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "-3.0")

    def test_division(self):
        ctrl = CalculatorController()
        ctrl.handle_button("9")
        ctrl.handle_button("/")
        ctrl.handle_button("2")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "4.5")

    def test_division_by_zero(self):
        ctrl = CalculatorController()
        ctrl.handle_button("15")
        ctrl.handle_button("/")
        ctrl.handle_button("0")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "Error")

    def test_factorial(self):
        ctrl = CalculatorController()
        ctrl.handle_button("5")
        ctrl.handle_button("!")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "120.0")

    def test_logarithm(self):
        ctrl = CalculatorController()
        ctrl.handle_button("1")
        ctrl.handle_button("0")
        ctrl.handle_button("log")
        ctrl.handle_button("1")
        ctrl.handle_button("0")
        ctrl.handle_button("0")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "2.0")

    def test_logarithm_dif_base(self):
        ctrl = CalculatorController()
        ctrl.handle_button("2")
        ctrl.handle_button("log")
        ctrl.handle_button("8")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "3.0")

    def test_power(self):
        ctrl = CalculatorController()
        ctrl.handle_button("2")
        ctrl.handle_button("^")
        ctrl.handle_button("3")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "8.0")

    def test_priority(self):
        ctrl = CalculatorController()
        ctrl.handle_button("2")
        ctrl.handle_button("+")
        ctrl.handle_button("3")
        ctrl.handle_button("*")
        ctrl.handle_button("4")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "14.0")

    def test_brackets_and_priority(self):
        ctrl = CalculatorController()
        ctrl.handle_button("(")
        ctrl.handle_button("2")
        ctrl.handle_button("+")
        ctrl.handle_button("3")
        ctrl.handle_button(")")
        ctrl.handle_button("*")
        ctrl.handle_button("4")
        ctrl.handle_button("=")
        self.assertEqual(ctrl.get_display_text(), "20.0")

    if __name__ == '__main__':
        unittest.main()