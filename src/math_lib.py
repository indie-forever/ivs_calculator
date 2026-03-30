import math 
import sys

class MathLib:
    """
    Matematická knižnica určená pre základné a pokročilé operácie.
    Obsahuje sčítanie, odčítanie, násobenie, delenie, faktoriál, 
    n-tú odmocninu, mocninu a dekadický logaritmus.
    Všetky výpočty prebiehajú v decimálnej sústave.
    """
    
    @staticmethod
    def add(a, b):
        """
        Vráti súčet dvoch čísel.
        
        Parametre:
            a (float/int) 
            b (float/int)
            
            
            
        Návratová hodnota:
        
            float/int: Súčet parametrov a + b.
        """
        return a + b
    
    @staticmethod
    def sub(a, b):
        """
        Vráti rozdiel dvoch čísel.
        
        Parametre:
            a (float/int)
            b (float/int) 

        Návratová hodnota:
            float/int: Rozdiel parametrov a - b.
        """
        return a - b
    
    @staticmethod
    def mul(a, b):
        """
        Vráti súčin dvoch čísel.
        
        Parametre:
            a (float/int)
            b (float/int)
            
        Návratová hodnota:
            float/int: Súčin parametrov a * b.
        """
        return a * b
    
    @staticmethod
    def div(a, b):
        """
        Vráti podiel dvoch čísel. Ošetruje delenie nulou.
        
        Parametre:
            a (float/int): Delenec.
            b (float/int): Deliteľ (nesmie byť 0).
            
        Návratová hodnota:
            float: Podiel a / b alebo None pri pokuse o delenie nulou.
        """
        #kontrola ci nedelime 0 
        if b == 0:
            sys.stderr.write("Chyba: Delenie nulou!\n") 
            return None
        return a / b

    
    @staticmethod
    def factorial(a):
        """
        Vypočíta faktoriál celého nezáporného čísla.
        
        Parametre:
            a (int/float): Číslo, z ktorého sa počíta faktoriál. 
                           Musí to byť celé nezáporné číslo.
            
        Návratová hodnota:
            int: Výsledok faktoriálu alebo None pri chybe.
        """
        # 1. Kontrola, či je to celé číslo
        if a % 1 != 0:
            sys.stderr.write("Error: Factorial takes only integer!\n")
            return None
        
        # 2. Kontrola, či nie je záporné 
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
        Vypočíta mocninu čísla. Podporuje celé exponenty .
        
        Parametre:
            base (float/int): Základ mocniny.
            exponent (int): Celé číslo .
            
        Návratová hodnota:
            float/int: Výsledok base^exponent alebo None pri chybe.
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
        Vypočíta n-tú odmocninu z čísla A.
        
        Parametre:
            A (float/int): Číslo, ktoré odmocňujeme.
            n (float/int): Stupeň odmocniny.
        Návratová hodnota:
            float: n-tá odmocnina z A alebo None pri chybe .
        """
        if n <= 0: sys.stderr.write("Error: Root degree must be positive\n"); return None
        if A < 0 and n % 2 == 0: sys.stderr.write("Error: Even root of negative number\n"); return None
        vysledok = math.pow(A, 1/n)
        return vysledok

    @staticmethod
    def log(a, x):
        """
        Vypočíta logaritmus čísla x o základe a.

        Parametre:
            a (float/int): Základ logaritmu .
            x (float/int): Číslo, ktorého logaritmus hľadáme .

        Návratová hodnota:
            float: Výsledok log_a(x) alebo None pri chybe .
        
        """
        if x <= 0: sys.stderr.write("Error: Logarithm argument x must be greater than 0\n"); return None
        if a <= 0 or a == 1: sys.stderr.write("Error: Logarithm base a must be greater than 0 and not equal to 1\n"); return None

        return math.log(x)/math.log(a)
    
       
    @staticmethod
    def dec_to_bin(dec:str):
        """
        
        """
        vysledok=""
        
        if "." in dec:
            cela, desatina = dec.split(".")
        #desatian cast
        
        if (desatina):
           pass

        #cela cast 
        if "-" in cela:
            pass

        dec = int(dec)
        while (dec > 0):
            zvysok = str(dec % 2 )
            dec //= 2 
            vysledok=vysledok + zvysok
        vysledok = vysledok[::-1]

    


        



        
    

    