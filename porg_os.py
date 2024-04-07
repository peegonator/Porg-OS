import time
import threading
import os
import subprocess

# ASCII art logo
logo = """
  _____ _   _ ____  _   _ _   _ ____  
 / ____| \ | |  _ \| | | | \ | |  _ \ 
| (___ |  \| | |_) | | | |  \| | | | |
 \___ \| . \` |  _ <| |_| | . \` | | | |
 ____) | |\  | |_) | |_| | |\  | | | |
|_____/|_| \_|____/ \___/|_| \_|____/ 
"""
print(logo)

# Setup logger (this part should be implemented in your logging module)
def setup_logger():
    pass

logger = setup_logger()

# Log boot message
logger.info('Booting Porg OS...')

# Simulate starting other services
def start_other_services():
    logger.info('Starting other services...')
    # Add other service startup routines here
    time.sleep(1)  # Simulate service startup time
    logger.info('Other services started.')

# Simulate stopping other services
def stop_other_services():
    logger.info('Stopping other services...')
    # Add other service shutdown routines here
    time.sleep(1)  # Simulate service shutdown time
    logger.info('Other services stopped.')

# Start other services
start_other_services()

# Main loop to keep the CLI running
while True:
    # Prompt user for action
    action = input('$ root@porgo ')

    # Check for exit command
    if action.lower() == 'exit':
        logger.info('Exiting...')
        # Stop other services
        stop_other_services()
        break

    # Execute the command
    logger.info(f'Executing command: {action}')
    # Handle commands
    if '|' in action:
        commands = action.split('|')
        output = None
        for cmd in commands:
            if output:
                cmd = cmd.strip() + ' ' + output
            output = subprocess.check_output(cmd.strip(), shell=True).decode('utf-8')
        print(output)
    elif action.lower() == 'ls':
        logger.info('Listing files in the user directory...')
        # List files in the user directory
        user_files = os.listdir('user')
        for file in user_files:
            logger.info(file)
    elif action.lower() == 'touch':
        filename = input('Enter filename: ')
        logger.info(f'Creating file: {filename}')
        # Create the file
        with open(f'user/{filename}', 'w') as f:
            pass
        logger.info(f'File {filename} created.')
    elif action.lower() == 'vi':
        filename = input('Enter filename to edit: ')
        logger.info(f'Opening file {filename} with vi...')
        try:
            subprocess.run(['vi', f'user/{filename}'])
        except FileNotFoundError:
            logger.error('vi command not found. Please make sure it is installed.')
    elif action.lower() == 'nano':
        filename = input('Enter filename to edit: ')
        logger.info(f'Opening file {filename} with nano...')
        try:
            subprocess.run(['nano', f'user/{filename}'])
        except FileNotFoundError:
            logger.error('nano command not found. Please make sure it is installed.')
    elif action.lower() == 'cd':
        directory = input('Enter directory: ')
        logger.info(f'Changing directory to {directory}...')
        # Placeholder for changing directory
    elif action.lower() == 'cat':
        filename = input('Enter filename to display: ')
        logger.info(f'Displaying contents of file {filename}...')
        # Placeholder for displaying file contents
        with open(f'user/{filename}', 'r') as f:
            contents = f.read()
            logger.info(contents)
    elif action.lower() == 'mkdir':
        dirname = input('Enter directory name: ')
        logger.info(f'Creating directory: {dirname}')
        # Create the directory
        os.makedirs(f'user/{dirname}')
        logger.info(f'Directory {dirname} created.')
    elif action.lower() == 'help':
        # Provide help information
        logger.info('Available commands:')
        logger.info('ls - List directory contents')
        logger.info('touch - Create a new file')
        logger.info('vi - Open a text editor')
        logger.info('nano - Open a text editor')
        logger.info('cd - Change directory')
        logger.info('cat - Display file contents')
        logger.info('mkdir - Create a new directory')
    else:
        logger.warning('Invalid command. Type "help" for available commands.')
