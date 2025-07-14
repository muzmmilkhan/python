import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app1.log")
## Configuring Logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the log message format
    datefmt='%Y-%m-%d %H:%M:%S',  # Define the date format
    handlers=[
        logging.FileHandler(LOG_FILE, mode='w'),  # Log messages will be written to this file
        logging.StreamHandler()  # Also output log messages to the console
    ]
)

logger = logging.getLogger("ArithmeticApp")  # Create a logger instance for the current module

def add(a, b):
    logger.debug(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    logger.debug(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    logger.debug(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    try:
        logger.debug(f"Dividing {a} by {b}")
        return a / b
    except ZeroDivisionError as e:
        logger.error(f"Error: Division by zero when dividing {a} by {b}")
        return None

def main():
    logger.info("Starting Arithmetic Operations")
    a, b = 10, 5
    logger.info(f"Performing operations with {a} and {b}")
    
    result_add = add(a, b)
    logger.info(f"Addition Result: {result_add}")
    
    result_subtract = subtract(a, b)
    logger.info(f"Subtraction Result: {result_subtract}")
    
    result_multiply = multiply(a, b)
    logger.info(f"Multiplication Result: {result_multiply}")
    
    result_divide = divide(a, b)
    if result_divide is not None:
        logger.info(f"Division Result: {result_divide}")
    
    logger.info("Arithmetic Operations Completed")

if __name__ == "__main__":
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)  # Create the log directory if it doesn't exist
    main()
    logger.info("Application finished running")