import logging
import os
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
date=f"{datetime.now().strftime('%d_%m_%Y')}"
log_path=os.path.join(os.getcwd(),"logs",date)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_Path=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_Path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

