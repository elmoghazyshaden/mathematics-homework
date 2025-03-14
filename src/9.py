import random

def get_random_code():
    numbers = list(range(10))
    operators = ["+", "-", "*", "/"]
    expression = ""
    for i in range(3):
        expression += str(random.choice(numbers)) + random.choice(operators)
    return expression[:-1]

get_random_code()