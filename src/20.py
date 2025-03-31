import math

def calculate_expression(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

expression1 = "5 * 7 + (3 - 2)"
expression2 = "math.sin(45) / math.cos(45)"

print(f"{calculate_expression(expression1)}")
print(f"{calculate_expression(expression2)}")
