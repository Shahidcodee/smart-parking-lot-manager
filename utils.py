import os
import logging

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def setup_logger():
    logging.basicConfig(filename='activity.log',
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO)

def log_activity(message):
    logging.info(message)

setup_logger()
