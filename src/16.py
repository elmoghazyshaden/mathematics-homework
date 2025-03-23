import numpy as np
def calculate_pi(num_points):
    x = np.random.rand(num_points)
    y = np.random.rand(num_points)
    pi_estimate = 4 * (1 - sum(x**2) / num_points) / sum(y**2)
    return pi_estimate

if __name__ == "__main__":
    # Example usage:
    print(calculate_pi(100))
