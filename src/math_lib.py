import math 
import sys

class MathLib:
    """
    @brief A mathematical library for basic and advanced arithmetic operations.
    @details Provides functionality for addition, subtraction, multiplication, 
    division, factorial, n-th root, power, and logarithms.
    """
    
    @staticmethod
    def add(a, b):
        """
        @brief Calculates the sum of two numbers.
        
        @param a The first number.
        @param b The second number.
        @return The result of a + b.
        """
        return a + b
    
    @staticmethod
    def sub(a, b):
        """
        @brief Calculates the difference between two numbers.
        
        @param a The initial value.
        @param b The value to subtract.
        @return The result of a - b.
        """
        return a - b
    
    @staticmethod
    def mul(a, b):
        """
        @brief Calculates the product of two numbers.
        
        @param a The first factor.
        @param b The second factor.
        @return The result of a * b.
        """
        return a * b
    
    @staticmethod
    def div(a, b):
        """
        @brief Calculates the quotient of two numbers with zero division check.
        
        @param a The dividend.
        @param b The divisor (must not be 0).
        @return The result of a / b, or None if division by zero is attempted.
        """
        #kontrola ci nedelime 0 
        if b == 0:
            sys.stderr.write("Error: Division by zero!\n") 
            return None
        return a / b

    
    @staticmethod
    def factorial(a):
        """
        @brief Calculates the factorial of a non-negative integer.
        
        @param a The number to calculate the factorial from (must be a non-negative integer).
        @return The factorial result, or None if the input is invalid.
        """
       
        if a % 1 != 0:
            sys.stderr.write("Error: Factorial takes only integer!\n")
            return None
        
       
        if a < 0:
            sys.stderr.write("Error: Factorial number must be 0 or higher!\n")
            return None
        
        a = int(a)
        vysledok = 1
        for i in range(1, a + 1):
            vysledok *= i

        return vysledok
    
    @staticmethod
    def pow(base, exponent):
        """
        @brief Calculates the power of a number.
        
        @param base The base of the power.
        @param exponent The exponent (must be an integer).
        @return The result of base^exponent, or None if the exponent is not an integer.
        """
        if exponent % 1 != 0: sys.stderr.write("Error: Exponent must be an integer\n"); return None
        
        if exponent == 0: return 1
        
        is_negative = exponent < 0
        abs_exp = int(abs(exponent))
        
        vysledok = 1
        for i in range(abs_exp):
            vysledok *= base
            
        if is_negative: return 1 / vysledok
        return vysledok
    
    
    @staticmethod
    def root(A, n):
        """
        @brief Calculates the n-th root of a number A.
        
        @param A The value to be rooted.
        @param n The degree of the root (must be positive).
        @return The n-th root of A, or None if parameters are invalid.
        """
        if n <= 0: sys.stderr.write("Error: Root degree must be positive\n"); return None
        if A < 0 and n % 2 == 0: sys.stderr.write("Error: Even root of negative number\n"); return None
        vysledok = math.pow(A, 1/n)
        return vysledok

    @staticmethod
    def log(a, x):
        """
        @brief Calculates the logarithm of x with base a.

        @param a The base of the logarithm (must be positive and not equal to 1).
        @param x The value to calculate the logarithm for (must be greater than 0).
        @return The result of log_a(x), or None if parameters are invalid.
        """
        if x <= 0: sys.stderr.write("Error: Logarithm argument x must be greater than 0\n"); return None
        if a <= 0 or a == 1: sys.stderr.write("Error: Logarithm base a must be greater than 0 and not equal to 1\n"); return None

        return math.log(x)/math.log(a)