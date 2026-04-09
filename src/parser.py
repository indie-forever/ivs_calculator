from math_lib import MathLib
import re

class ExpressionParser:
    def parse_and_calc(self, expression):
        try:
            while "(" in expression:
                expression = re.sub(r'\(([^()]+)\)',
                    lambda m: str(self.parse_and_calc(m.group(1))), expression)
            
            tokens = re.findall(r'\d+\.?\d*|[+\-*/!*^()]|log|root', expression)
            if not tokens: return "0"

            tokens = self.process_unaries(tokens)
            tokens = self.process_op(tokens, ["^", "root"])
            tokens = self.process_op(tokens, ["log"])
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

                res = None
                if op == "+": res = MathLib.add(left, right)
                elif op == "-": res = MathLib.sub(left, right)
                elif op == "*": res = MathLib.mul(left, right)
                elif op == "/": res = MathLib.div(left, right)
                elif op == "^": res = MathLib.pow(left, right)
                elif op == "root": res = MathLib.root(left, right)
                elif op == "log": res = MathLib.log(left, right)

                if res is None:
                    raise Exception("Math Error")

                tokens[i-1:i+2] = [res]

                i -= 1
            i += 1
        return tokens