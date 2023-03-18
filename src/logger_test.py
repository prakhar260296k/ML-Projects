import logging
import os
from datetime import datetime

## Now we need to create log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ## Naming convention of the file we create
## We need to give path of the log file
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) ## Each file will start with logs followed by file_name
os.makedirs(logs_path,exist_ok=True) ## Even if there is a file, folder just keep on updating it

LOGS_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


if __name__ == "__main__":
    logging.info("Logging has started")
