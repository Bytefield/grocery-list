import logging
import sys

class Logger:
    """A simple logger class that logs messages"""
    def __init__(self, name, log_file='app.log', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create a file handler
        handler = logging.FileHandler(log_file)
        handler.setLevel(level)

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(handler)

    def log(self, message, level=logging.INFO):
        if level == logging.CRITICAL:
            self.logger.critical(message)
            sys.exit(1)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.INFO:
            self.logger.info(message)
        else:
            self.logger.debug(message)