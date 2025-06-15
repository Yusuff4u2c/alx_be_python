def safe_divide(numerator, denominator):
    
    try:
        return float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Please enter numeric values only.")
        return None