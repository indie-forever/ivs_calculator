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
        