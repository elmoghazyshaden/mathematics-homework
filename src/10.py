
import random

def get_random_math_problem(operator):
    numbers = [1, 2, 3, 4, 5]
    number1 = random.choice(numbers)
    number2 = random.choice(numbers)
    if operator == '+':
        return f'{number1} + {number2}'
    elif operator == '-':
        return f'{number1} - {number2}'
    elif operator == '*':
        return f'{number1} * {number2}'
    else:
        return None

print(get_random_math_problem('+'))