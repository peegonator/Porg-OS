# users/sshd.py

import time
from cli.logging import setup_logger

# Setup logger
logger = setup_logger()

def start_sshd():
    logger.info('Starting SSH daemon (sshd) service...')
    # Placeholder for starting SSH daemon
    time.sleep(1)  # Simulate service startup time
    logger.info('SSH daemon (sshd) service started.')

def stop_sshd():
    logger.info('Stopping SSH daemon (sshd) service...')
    # Placeholder for stopping SSH daemon
    time.sleep(1)  # Simulate service shutdown time
    logger.info('SSH daemon (sshd) service stopped.')
