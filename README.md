# SCT_CS_4
Skillcraft technology internship in cyber security task 4)  Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file.

# Key Logger Using `pynput`

This Python script is a simple key logger that records key presses and saves them to a text file. It uses the `pynput` library to listen to keyboard events.

---

## Features
- Logs character keys (e.g., `a`, `b`, `c`).
- Logs special keys (e.g., `Enter`, `Space`, `Shift`).
- Saves the logs to a file named `key_log.txt`.

---

## Prerequisites
- Python 3.x
- `pynput` library for capturing keyboard events.

---

## Steps to Run on Kali Linux

1. **Open the Terminal.**
2. **Install Python (if not already installed):**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
3. **Install pynput (if not already installed):**
   ```bash
   pip3 install pynput

4. **Open the Terminal.**
   ```bash
   python3 SCT_CS_4.py
