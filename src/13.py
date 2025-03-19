def get_random_math_problem():
    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Ask the user for the correct answer
    answer = int(input("What is {} x {}?".format(num1, num2)))
    
    # Check if the answer is correct
    if answer == num1 * num2:
        print("Correct! The answer is {}. Good job!".format(num1 * num2))
    else:
        print("Sorry, that's incorrect. The correct answer is {}.".format(num1 * num2))
