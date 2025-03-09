import random

def get_random_number(max_value):
    return random.randint(0, max_value)

def get_random_operation():
    operations = ['+', '-', '*', '/']
    return random.choice(operations)

def get_random_expression(max_value):
    left = get_random_number(max_value)
    right = get_random_number(max_value)
    operation = get_random_operation()
    return f"{left} {operation} {right}"

def evaluate_expression(expression):
    left, operation, right = expression.split(" ")
    left = int(left)
    right = int(right)
    if operation == "+":
        result = left + right
    elif operation == "-":
        result = left - right
    elif operation == "*":
        result = left * right
    else:
        result = left / right
    return result

if __name__ == "__main__":
    max_value = 100
    for i in range(5):
        expression = get_random_expression(max_value)
        print(f"{i+1}. {expression} = {evaluate_expression(expression)}")
