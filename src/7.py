def math_homework():
    # Generate a random problem
    problem = random.choice(["Addition", "Subtraction", "Multiplication", "Division"])
    
    # Generate two random numbers for the problem
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    
    if problem == "Addition":
        return num1 + num2
    elif problem == "Subtraction":
        return num1 - num2
    elif problem == "Multiplication":
        return num1 * num2
    else:
        return num1 / num2
