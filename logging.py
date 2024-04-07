# cli/logging.py

import logging

def setup_logger():
    # Create logger
    logger = logging.getLogger('PorgOS')
    logger.setLevel(logging.DEBUG)

    # Create console handler and set level to DEBUG
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Create formatter
    formatter = logging.Formatter('%(levelname)s %(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # Add formatter to console handler
    ch.setFormatter(formatter)

    # Add console handler to logger
    logger.addHandler(ch)

    return logger
