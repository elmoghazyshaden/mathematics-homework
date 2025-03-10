
import math

def calculate_area(shape):
    if shape == "circle":
        radius = float(input("Enter the circle's radius: "))
        return math.pi * radius ** 2
    elif shape == "square":
        side = float(input("Enter the square's side length: "))
        return side * side
    else:
        print("Invalid shape. Please enter either 'circle' or 'square'.")
