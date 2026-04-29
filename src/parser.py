##
# @file parser.py
# @author Simona Studená (xstudes00)
# @brief Mathematical expression parser and evaluator.
#

from math_lib import MathLib
import re

##
# @class ExpressionParser
# @brief Class responsible for parsing strings into mathematical operations.
#
class ExpressionParser: 
    ##
    # @brief Parses the string and calculates the result with respect to parentheses and priority.
    # @param expression The mathematical string to evaluate.
    # @return The result as a string or "Error" on failure.
    #
    def parse_and_calc(self, expression):
        try:
            # Recursive Parentheses Resolution
            while "(" in expression:
                # Regex explanation: r'\(([^()]+)\)'
                # \( and \) : Matches the literal "(" and ")" characters in the math expression.
                # (...)     : Capture group (accessible via m.group(1)).
                # [^()]     : Negated set - matches any character EXCEPT opening or closing brackets.
                # +         : Quantifier - matches one or more of the preceding characters.
                # Pattern: matches the innermost pairs of parentheses containing no other parentheses.
                expression = re.sub(r'\(([^()]+)\)',
                    # Lambda function captures group(1) (content inside parentheses) and passes it recursively back to parse_and_calc.
                    lambda m: str(self.parse_and_calc(m.group(1))), expression)
            
            # Tokenize: Split the string into a list of individual tokens.
            # Regex explanation: r'\d+\.?\d*|[+\-*/!*^()]|log|root'
            # \d+\.?\d*     : Numeric literals (one or more digits, optional floating point, zero or more digits).
            # [+\-*/!^()]   : Single character operators and brackets.
            # log|root      : Multi character function names.
            tokens = re.findall(r'\d+\.?\d*|[+\-*/!^()]|log|root', expression)
            if not tokens: return "0"

            processed_tokens = []
            i = 0
            while i < len(tokens):
                # If '-' is the first symbol or right after parentheses or an operator, the number after is negative.
                if tokens[i] == '-' and (i == 0 or tokens[i-1] in "+-*/(^logroot"):
                    if i + 1 < len(tokens):
                        processed_tokens.append("-" + tokens[i+1])
                        i += 2
                        continue
                processed_tokens.append(tokens[i])
                i += 1
            tokens = processed_tokens

            # Apply operations in order of mathematical priority.
            tokens = self.process_unaries(tokens)
            tokens = self.process_op(tokens, ["^", "root"])
            tokens = self.process_op(tokens, ["log"])
            tokens = self.process_op(tokens, ["*", "/"])
            tokens = self.process_op(tokens, ["+", "-"])

            # The last ramining token is the result.
            return tokens[0]
        except Exception:
            return "Error"
        
    ##
    # @brief Processes unary operators in the token list.
    # @param tokens List of mathematical tokens in the string.
    # @return A new list of tokens with unary operations resolved.
    #
    def process_unaries(self, tokens):
        new_tokens = []
        i = 0
        while i < len(tokens):
            if tokens [i] == "!":
                # Removes the last added number from new_tokens to use it as an operand.
                last_val = int(float(new_tokens.pop()))
                # Calculate factorial via MathLib and push the result back to the list.
                new_tokens.append(MathLib.factorial(last_val))
            else:
                new_tokens.append(tokens[i])
            i +=1
        return new_tokens
    
    ##
    # @brief Processes binary operators based on precedence.
    # @param tokens Current list of expression tokens.
    # @param ops A list of operators to process in this pass.
    # @return A reduced list of tokens with the binary operations resolved.
    #
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
                # Replace both operands and the operator all with one element, the result.
                tokens[i-1:i+2] = [res]
                # Hence the list is now shorter, we need to check again the last index.
                i -= 1
            i += 1
        return tokens