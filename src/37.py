def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    
    y = 2.0
    while True:
        half_squared = y * y
        if half_squared > x:
            return half_squared - (half_squared - x) / 2.0

# Example usage:
x = 16
result = square_root(x)
print(f"The square root of {x} is approximately: {result}")
