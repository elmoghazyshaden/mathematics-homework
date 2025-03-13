  import random
  def get_random_code():
   num1 = random.randint(1,10)
   num2 = random.randint(1,10)
   operation = random.choice(['+', '-', '*'])
   if operation == '+':
    return f'{num1} + {num2}'
   elif operation == '-':
    return f'{num1} - {num2}'
   else:
    return f'{num1} * {num2}'