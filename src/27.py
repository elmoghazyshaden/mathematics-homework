# Exercise 1: Summation
total = sum(range(10))  # 55

# Exercise 2: Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci_sequence = [fibonacci(i) for i in range(1, n+1)]
print(f"Fibonacci sequence up to {n} terms:")
for num in fibonacci_sequence:
    print(num)
