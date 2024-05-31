---
# Keylogger Tool

A simple keylogger that logs keystrokes for a specified duration and saves them to a file.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)
- [Contributing](#contributing)

## Overview

This keylogger tool captures keystrokes for a user-defined duration and saves the logged keys to a file named `keylog.txt`. It uses the `pynput` library to listen for keyboard events.

## Features

- **Keylogging:** Capture keystrokes and store them in a buffer.
- **Duration Control:** Run the keylogger for a specified amount of time.
- **File Logging:** Save the captured keystrokes to `keylog.txt`.
- **Real-time Feedback:** Display remaining time in the console.

## Installation

To set up this project, you need to have Python installed on your machine. Follow the steps below:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/keylogger-tool.git
   ```
   
2. **Navigate to the project directory:**
   ```sh
   cd keylogger-tool
   ```

3. **Install required dependencies:**
   ```sh
   pip install pynput
   ```

4. **Run the keylogger:**
   ```sh
   python keylog.py
   ```

## Usage

1. **Run the keylogger script:**
   ```sh
   python keylog.py
   ```

2. **Enter the duration:**
   - You will be prompted to enter the duration for which you want the keylogger to run (in seconds).

3. **Keylogger in action:**
   - The keylogger will start and capture all keystrokes for the specified duration.
   - The remaining time will be displayed in the console.

4. **Completion:**
   - After the duration ends, the captured keystrokes will be saved to `keylog.txt`.

## Example

### Running the Keylogger
```sh
$ python keylog.py
Enter the duration for which you want to run the keylogger (in seconds):
10
Time duration to run: 10 seconds
Remaining time: 9 seconds
Remaining time: 8 seconds
...
Remaining time: 1 second
Keys logged to 'keylog.txt'
```

### Checking the Logged Keys
```sh
$ cat keylog.txt
hello world
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
