def calculate_area(shape):
    if shape == "circle":
        radius = 10
        area = 3.14 * (radius ** 2)
        print(f"The area of a circle with radius {radius} is: {area}")
    elif shape == "rectangle":
        length = 5
        width = 3
        area = length * width
        print(f"The area of a rectangle with length {length} and width {width} is: {area}")
    else:
        print("Invalid shape")

calculate_area(shape="circle")
calculate_area(shape="rectangle")
