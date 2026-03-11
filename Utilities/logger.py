import logging
import os

def get_logger():

    if not os.path.exists("logs"):
        os.makedirs("logs")

    logger = logging.getLogger("FlightAutomation")
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("logs/automation.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger