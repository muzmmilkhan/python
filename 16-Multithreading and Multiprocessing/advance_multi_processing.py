## Advance  Multiprocessing with Process Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(n):
    """Function to square a number with a delay."""
    time.sleep(2)  # Simulate a time-consuming task
    return n * n

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        # Map the square_number function to the numbers list
        results = executor.map(square_number, numbers)

    for result in results:
        print(result)