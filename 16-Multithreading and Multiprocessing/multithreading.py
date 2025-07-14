### Multithreading
# When to use multithreading:
# - When you have I/O-bound tasks (e.g., network requests, file I/O) that can benefit from concurrent execution.
# - When you want to improve the responsiveness of your application by allowing other tasks to run while waiting for I/O operations to complete.
# - When you need to perform multiple tasks simultaneously, such as handling user input while processing data in the background.

# When not to use multithreading:
# - When you have CPU-bound tasks that require heavy computation, as Python's Global Interpreter Lock (GIL) can limit the performance benefits of multithreading.
# - When your tasks are not I/O-bound and can be executed sequentially without significant performance impact.
# - When you need to perform tasks that require strict ordering or synchronization, as multithreading can introduce complexity

import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(2)  # Simulate a delay

def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(2)  # Simulate a delay


# Create threads for each function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

t = time.time()
# Start the threads
thread1.start()
thread2.start()
# Wait for both threads to complete
thread1.join()
thread2.join()
finish_time = time.time()
print(f"Total time taken: {finish_time - t:.2f} seconds")