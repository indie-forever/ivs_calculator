from math_lib import MathLib

class CalculatorController:
    def __init__(self):
        self.display_value = "0"
        self.first_number = None
        self.operation = None

    def handle_button(self, value):
        if value.isdigit():
            if self.display_value == "0":
                self.display_value = value
            else:
                self.display_value += value

        elif value == "C":
            self.display_value = "0"
            self.first_number = None
            self.operation = None

    def get_display_text(self):
        return self.display_value

