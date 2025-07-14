import logging

LOG_DIR = 'logs'  # Directory where log files will be stored
# Ensure the log directory exists
import os
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

log_file = os.path.join(LOG_DIR, 'app.log')

# Configure logging
logging.basicConfig(
    filename=log_file,  # Log messages will be written to this file
    filemode='w',  # 'w' for write mode, 'a' for append mode
    level=logging.DEBUG,  # Set the logging level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Define the date format
)