### Advanced Multithreading Techniques
# Thread pool Executor is a high-level interface for managing a pool of threads, allowing you to submit tasks that will be executed by the threads in the pool. 
# It simplifies the process of creating and managing threads, making it easier to write concurrent code.

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(num):
    """Function to print numbers with a delay."""
    time.sleep(1)  # Simulate a delay
    print(f"Number: {num}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

for result in results:
    print(result)  # This will print None since print_numbers does not return anything