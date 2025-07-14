'''
Real World Use Case: Multiprocessing for cpu-bound tasks
Scenario: Factorial Calculation
Description: This code demonstrates how to use the multiprocessing module to calculate factorials of a list of numbers in parallel. Each factorial calculation is a CPU-bound task, and using multiprocessing allows us to utilize multiple CPU cores for better performance.
'''

import multiprocessing
import time
import sys
import math

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(1000000)

# Function to calculate factorial
def compute_factorial(n):
    print(f"Calculating factorial of {n}")
    time.sleep(1)  # Simulate a time-consuming task
    return math.factorial(n)

if __name__ == "__main__":
    numbers = [10000, 20000, 30000, 40000, 50000]  # List of numbers to calculate factorials for

    start_time = time.time()
    print("Starting factorial calculations...")
    # Create a pool of worker processes
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Map the compute_factorial function to the list of numbers
        results = pool.map(compute_factorial, numbers)

    print("Factorials calculated:", results)
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.2f} seconds")