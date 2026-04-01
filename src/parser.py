from math_lib import MathLib
import re

class ExpressionParser:
    def parse_and_calc(self, expression):
        try:
            tokens = re.findall(r'\d+\.?d*|[+\-*/!]|log', expression)
            tokens = self.process_unaries(tokens)

            tokens = self.process_op(tokens, ["*", "/"])
            tokens = self.process_op(tokens, ["+", "-"])

            return tokens[0]
        except Exception:
            return "Error"
        
    def process_unaries(self, tokens):
        new_tokens = []
        i = 0
        while i < len(tokens):
            if tokens [i] == "!":
                last_val = int(float(new_tokens.pop()))
                new_tokens.append(MathLib.factorial(last_val))
            elif tokens[i] == "log":
                last_val = float(new_tokens.pop())
                new_tokens.append(MathLib.log(10, last_val))
            else:
                new_tokens.append(tokens[i])
            i +=1
        return new_tokens
    
    def process_op(self, tokens, ops):
        i = 0
        while i < len(tokens):
            if tokens[i] in ops:
                left = float(tokens[i-1])
                op = tokens[i]
                right = float(tokens[i+1])

                if op == "+": res = MathLib.add(left, right)
                elif op == "-": res = MathLib.sub(left, right)
                elif op == "*": res = MathLib.mul(left, right)
                elif op == "/": res = MathLib.div(left, right)

                if res is None:
                    raise Exception("Math Error")

                tokens[i-1:i+2] = [res]

                i -= 1
            i += 1
        return tokens