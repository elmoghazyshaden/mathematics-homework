def find_factors(n):
    """
    Find all factors of a given number n.
    
    Parameters:
    n (int): The number to find factors for.
    
    Returns:
    list: A list containing all factors of n.
    """
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

# Example usage
n = 36
print("Factors of", n, ":", find_factors(n))
