import logging
import os


class Logger:
    @staticmethod
    def get_logger():
        if not os.path.exists('logs'):
            os.mkdir('logs')

        logger = logging.getLogger('SauceDemo')

        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler('logs/test.log')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger