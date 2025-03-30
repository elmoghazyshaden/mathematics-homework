# Question 1: 
def find_max_value(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

numbers = [4, 8, -2, 6, 9, 10]
print(find_max_value(numbers))

# Question 2: 
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

prime_numbers = [number for number in range(2, 31) if is_prime(number)]
print(prime_numbers)

# Question 3: 
def calculate_mean(numbers):
    sum_numbers = sum(numbers)
    mean = sum_numbers / len(numbers)
    return mean

numbers = [1.5, 2.5, 3.5]
mean = calculate_mean(numbers)
print(mean)

