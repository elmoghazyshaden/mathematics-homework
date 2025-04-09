def square_root(x):
    return x ** 0.5

def area_circle(radius):
    return 3.14159 * radius ** 2

def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(1, n):
            a, b = b, a + b
        return b

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

def main():
    print("Square root of x:", square_root(4))
    print("Area of circle with radius 5:", area_circle(5))
    print("Fibonacci number for n=4:", fibonacci(4))
    print("Binary search result:", binary_search([3, 5, 7, 9], 6))

if __name__ == "__main__":
    main()
