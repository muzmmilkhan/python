## Multiprocessing in Python
# Multiprocessing in Python allows the creation of multiple processes, enabling parallel execution of tasks. 
# This is particularly useful for CPU-bound tasks (mathematical computations, data processing), as it can significantly improve performance by utilizing multiple CPU cores. 
# The `multiprocessing` module provides a simple and effective way to create and manage processes, share data between them, and synchronize their execution.

import multiprocessing
import time

def square_number():
    """Function to square a number."""
    for i in range(10):
        time.sleep(0.1)  # Simulate a time-consuming task
        print(f"Square of {i} is {i * i}")

def cube_number():
    """Function to cube a number."""
    for i in range(10):
        time.sleep(0.1)  # Simulate a time-consuming task
        print(f"Cube of {i} is {i * i * i}")

if __name__ == "__main__":
    # Create processes for each function
    process1 = multiprocessing.Process(target=square_number)
    process2 = multiprocessing.Process(target=cube_number)

    t = time.time()
    print(f"Starting processes at {t}")
    # Start the processes
    process1.start()
    process2.start()

    # Wait for both processes to complete
    process1.join()
    process2.join()
    print(f"Processes completed at {time.time() - t} seconds")