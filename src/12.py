import random

def get_random_math_problem():
    # Generate a random math problem
    op = random.choice(["+", "-", "*", "/"])
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 / num2

# Test the function with a random problem
print(get_random_math_problem())
