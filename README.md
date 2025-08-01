# Save Open Tabs

## Overview

`save_open_tabs.py` is a Python script that automates the process of saving the URLs of all open browser tabs to a text file on the Desktop. Each URL is saved on a separate line, and the script ensures that no duplicate files overwrite existing ones by appending a numeric suffix (e.g., open_tabs_1.txt) when needed. The script includes robust error handling, such as browser detection, URL validation with retries, and a timeout mechanism to prevent infinite loops.

## Features
- Saves URLs from open browser tabs to a text file on the Desktop.
- Supports multiple platforms (Windows, macOS, Linux).
- Generates unique filenames to avoid overwriting existing files.
- Detects if a browser window is active before starting.
- Includes retries for invalid or empty URLs and a maximum execution time for safety.
- Configurable pause times for compatibility with different systems.

## Requirements
Python 3.6 or higher


### Required Python packages:
- pyautogui
- pyperclip
- psutil

## Installation
- Ensure Python is installed on your system. You can download it from python.org.
- Install the required packages using pip:
- pip install pyautogui pyperclip psutil
- Save the script as save_open_tabs.py in a directory of your choice.

## Usage
- Open your web browser (e.g., Chrome, Firefox, Edge, Safari, Opera) with the tabs you want to save.
- Run the script from the command line:
- python save_open_tabs.py
- Within 3 seconds, click on the browser window to bring it into focus. Avoid using the keyboard or mouse while the script runs.

## The script will:
- Iterate through all open tabs using Ctrl+Tab (Windows) or Cmd+Tab (macOS/Linux).
- Copy each tab's URL and save it to a file named open_tabs.txt on your Desktop.
- If open_tabs.txt already exists, it will create a new file like open_tabs_1.txt.
- Check the Desktop for the output file, which contains the URLs, one per line.

## Configuration
- Pause Times: The script uses short pause times (pyautogui.PAUSE = 0.01 and time.sleep(0.005)) for speed. If you encounter issues (e.g., empty URLs), increase these values (e.g., to 0.02 and 0.01).
- Maximum Tabs: The script limits processing to 100 tabs (max_tabs = 100) to prevent infinite loops. Adjust this value if needed.
- Execution Timeout: The script stops after 60 seconds (max_execution_time = 60) to avoid hangs. Modify this value for more tabs.
- Browser Detection: The script checks for common browsers (Chrome, Firefox, Edge, Safari, Opera). Add other browser names to the browser_processes list in is_browser_active() if needed.

## Notes
- Safety Feature: Move the mouse to the top-left corner of the screen to stop the script immediately (via pyautogui.FAILSAFE).
- Compatibility: Works best with browsers that support Ctrl+L/Cmd+L (select address bar) and Ctrl+Tab/Cmd+Tab (switch tabs). Test with your browser to ensure compatibility.

## Troubleshooting
- If the script skips tabs or saves empty URLs, increase the pause times.
- If no browser is detected, ensure the browser window is in focus before the script starts.
- Add print(f"Tab {i + 1}: {url}") after url = pyperclip.paste().strip() to debug captured URLs.
- Alternative: For more robust automation, consider using Selenium to control the browser directly, though it requires additional setup.

## License

This project is licensed under the MIT License. Feel free to modify and distribute as needed.

## Author
Omar Andrés Ibarra Olivas
Developed with assistance from Grok, created by xAI.
