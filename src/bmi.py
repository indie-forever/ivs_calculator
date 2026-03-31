import sys

def bmi(height_cm, weight):
    """
    Calculate the Body Mass Index .

    Args:
        height_cm (float or int): Height of the person in centimeters.
        weight (float or int): Weight of the person in kilograms.

    Returns:
        float: Calculated BMI value.
        None: If the height is zero or invalid.
    """
    if height_cm <= 0 or weight <= 0:
        sys.stderr.write("Error: Invalid input. Height and weight must be greater than zero.\n")
        return None
    
    height_m = height_cm / 100
    return weight / (height_m ** 2)