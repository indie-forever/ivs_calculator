##
# @file logic.py
# @author Simona Studená (xstudes00)
# @brief Controller for managing calculator logic and UI interaction.
#

from parser import ExpressionParser

##
# @class CalculatorController
# @brief Coordinates interaction between the user interface and the expression parser.
#
class CalculatorController:
    ##
    # @brief Initializes the controller with default display and expression values.
    #
    def __init__(self):
        ## @var display_value Current string shown on the calculator display.
        self.display_value = "0"
        ## @var expression Internal string representing the full mathematical expression.
        self.expression = ""

    ##
    # @brief Handles button clicks from the UI and updates the internal state.
    # @param value The value of the button pressed (number, operator, or command).
    #
    def handle_button(self, value):
        # Handle numbers and decimal points.
        if value.isdigit() or value == ".":
            if self.display_value == "0" and value != ".":
                self.display_value = value
            else:
                self.display_value += value
            self.expression += value

        # Handle operators
        elif value in ["+", "-", "*", "/", "^", "root", "(", ")", "!", "log"]:
            self.expression += value
            self.display_value = "0"

        # Handle clear command.
        elif value == "C":
            self.display_value = "0"
            self.expression = ""

        # Handle evaluation command
        elif value == "=":
            parser = ExpressionParser()
            result = parser.parse_and_calc(self.expression)
            # Try to format as float string.
            try:
                formatted_res = str(float(result))
                self.display_value = formatted_res
            # In a case of error, display a string.
            except (ValueError, TypeError):
                self.display_value = str(result)

            # Update expression for further calculations.
            self.expression = self.display_value

    ##
    # @brief Returns the current text to be displayed on the calculator.
    # @return String containing the current display value.
    #
    def get_display_text(self):
        return self.display_value