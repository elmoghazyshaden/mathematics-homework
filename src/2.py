
import math
def calculate_area(shape):
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        return area
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        return area
    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = (base * height) / 2
        return area
    else:
        print("Invalid shape. Please enter either 'circle', 'rectangle', or 'triangle'.")

shape = input("Enter the shape you want to calculate the area for: ")
area = calculate_area(shape)
print(f"The area of the {shape} is {area}")