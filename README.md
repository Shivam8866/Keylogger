# Keylogger
This is a simple keylogger written in Python using the `pynput` library. It logs every key pressed on the keyboard and saves the keystrokes to a log file for later review.

> ⚠️ **Warning:** This tool is for **educational** and **ethical use only**. Unauthorized use of keyloggers is **illegal and unethical**.

---

## Features

- Captures and logs every key press
- Stores logs with timestamps
- Saves logs to a specified directory
- Minimal and easy to understand code

---

## Requirements

- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/)

Install the required package:

```bash
pip install pynput
```
Log File Location
The log file is saved to:

bash
Copy
Edit
D:/keylogger/log/keylog.txt
Ensure the directory exists before running the script, or update the log_file variable in the code:

python
Copy
Edit
log_file = "D:/keylogger/log/"
Usage
Clone or download the script.

Update the path to your desired log folder.

Run the script:

bash
Copy
Edit
python keylogger.py
The keylogger will start in the background and log every key press to the specified file.

Stopping the Logger
To stop the keylogger, interrupt the script manually using Ctrl + C in the terminal or stop the Python process from your task manager.

Disclaimer
This script is intended only for educational purposes, such as learning about cybersecurity, penetration testing, or monitoring authorized environments (e.g., your own systems).

Do not use this tool on someone else's device or network without explicit consent.

Misuse of this tool may lead to legal consequences.

License
This project is open for modification and learning. Do not use it for unethical or unauthorized surveillance.
