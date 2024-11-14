import logging
import os # (providing functionalities to writing in and reading from the file)
from datetime import datetime
# Create a log file
LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'

# Create a path to dump the log
logs_path=os.path.join(os.getcwd(), 'logs', LOG_FILE) # It'll join all different paths 

# to store all files
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)