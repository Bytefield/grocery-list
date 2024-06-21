import logging
import sys

class Logger:
    """A simple logger class that logs messages"""
    def __init__(self, log_file='app.log', level='INFO'):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.get_log_level(level))

        # Create a file handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(self.get_log_level(level))

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(self.get_log_level(level))

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_log_level(self, level):
        levels = {
            'CRITICAL': logging.CRITICAL,
            'ERROR': logging.ERROR,
            'WARNING': logging.WARNING,
            'INFO': logging.INFO,
            'DEBUG': logging.DEBUG
        }
        return levels.get(level.upper(), logging.INFO)

    def critical(self, message):
        self.logger.critical(message)
        sys.exit(1)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)