# create a reusable logger function that can be used across the application
import logging


def get_logger_info(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler = logging.FileHandler("info.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
