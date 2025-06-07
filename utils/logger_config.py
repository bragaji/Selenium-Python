import logging
import os

def get_logger(name="selenium-pom"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # Ensure logs/ directory exists at project root
        logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
        os.makedirs(logs_dir, exist_ok=True)

        log_file = os.path.join(logs_dir, "test_log.log")

        # Handlers
        console = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file, mode='a')

        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        console.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console)
        logger.addHandler(file_handler)

    return logger
