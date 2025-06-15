def safe_divide(numerator, denominator):
    
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Both numerator and denominator must be numbers.")
        return None