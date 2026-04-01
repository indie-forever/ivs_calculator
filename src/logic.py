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

        elif value in ["+", "-", "*", "/"]:
            self.first_number = float(self.display_value)
            self.operation = value
            self.display_value = "0"

        elif value == "=":
            if self.first_number is not None and self.operation is not None:
            
                try:
                    second_number = float(self.display_value)

                    if self.operation == "+":
                        result = MathLib.add(self.first_number, second_number)
                    
                    elif self.operation == "-":
                        result = MathLib.sub(self.first_number, second_number)

                    elif self.operation == "*":
                        result = MathLib.mul(self.first_number, second_number)

                    elif self.operation == "/":
                        result = MathLib.div(self.first_number, second_number)
                    
                    if result is None:
                        self.display_value = "Error"
                    else:
                        self.display_value = str(result)

                except ZeroDivisionError:
                    self.display_value = "Error"
                except Exception:
                    self.display_value = "Error"

                self.first_number = None
                self.operation = None

        elif value == "!":
            try:
                n = int(float(self.display_value))
                result = MathLib.factorial(n)
                self.display_value = str(float(result))
            except Exception:
                self.display_value = "Error"

        elif value == "log":
            try:
                x = float(self.display_value)
                result = MathLib.log(10, x)
                if result is None:
                    self.get_display_value = "Error"
                else:
                    self.display_value = str(float(result))

            except Exception:
                self.display_value = "Error"

        elif value == "C":
            self.display_value = "0"
            self.first_number = None
            self.operation = None

    def get_display_text(self):
        return self.display_value

