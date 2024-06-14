import logging
import pytest


@pytest.mark.usefixtures("setup", "get_test_data")
class BaseClass:
    """BaseClass to hold all the common utilities"""

    def get_logger(self):
        """This method can be used to log all the events to a separate log file"""
        logger = logging.getLogger(__name__)  # __name returns the test case at run time
        handler = logging.FileHandler(
            filename="C:\\Users\\deybi\\PycharmProjects\\WebAutomation\\Logs\\logs.txt"
        , mode='w')  # code responsible for the creation of log file
        formatter = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
        )  # code responsible to initialize the log format
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)  # DEBUG INFO WARNING CRITICAL ERROR
        return logger
