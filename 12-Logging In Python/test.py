from logger import logging

def add(x, y):
    logging.debug(f"Adding {x} and {y}")
    return x + y


if __name__ == "__main__":
    logging.info("Starting the addition process")
    result = add(5, 3)
    logging.info(f"The result of the addition is {result}")
    logging.warning("This is a warning message for demonstration purposes")
    logging.error("This is an error message for demonstration purposes")
    logging.critical("This is a critical message for demonstration purposes")
    logging.debug("Debugging information: Addition completed successfully")
    logging.info("Exiting the program")