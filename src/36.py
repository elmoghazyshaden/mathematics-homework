def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def subtract_numbers(a, b):
    """Subtract one number from another"""
    return a - b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b

def divide_numbers(a, b):
    """Divide one number by another"""
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero")
