def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return the result.
    
    Example usage:
    >>> add_numbers(2, 3)
    5
    >>> add_numbers(-1, 1)
    0
    """
    return a + b

def square_root(number: float) -> float:
    """
    Calculate the square root of a number and return it.
    
    Example usage:
    >>> square_root(25.0)
    5.0
    """
    return math.sqrt(number)

print(add_numbers(10, 20))
print(square_root(-4.5))
