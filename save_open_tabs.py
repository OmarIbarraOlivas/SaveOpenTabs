import pyautogui
import pyperclip
import time
import os
import psutil
import sys

# Initial setup
pyautogui.FAILSAFE = True  # Move the mouse to the top-left corner to stop the script
pyautogui.PAUSE = 0.01  # Adjusted pause time as per user preference

def get_unique_filename(base_path):
    """Generate a unique filename if one with the same name already exists."""
    base, ext = os.path.splitext(base_path)
    counter = 1
    new_path = base_path
    while os.path.exists(new_path):
        new_path = f"{base}_{counter}{ext}"
        counter += 1
    return new_path

def is_browser_active():
    """Attempt to detect if the active window is a browser."""
    try:
        # List of common browser process names
        browser_processes = ['chrome', 'firefox', 'edge', 'safari', 'opera']
        for proc in psutil.process_iter(['name']):
            if any(browser.lower() in proc.info['name'].lower() for browser in browser_processes):
                return True
        print("Warning: No active browser detected. Ensure the browser window is selected.")
        return False
    except Exception as e:
        print(f"Error checking active window: {e}")
        return False

def save_open_tabs(output_file=os.path.join(os.path.expanduser("~"), "Desktop", "open_tabs.txt"), max_execution_time=60):
    """Save the URLs of open browser tabs to a text file."""
    # Generate a unique filename if the file already exists
    output_file = get_unique_filename(output_file)
    
    # Set for unique URLs and list to maintain order
    seen_urls = set()
    links = []
    
    # Ensure the browser is in focus
    print("Please click on the browser window and avoid using the keyboard/mouse.")
    time.sleep(3)  # Initial wait time to activate the browser
    if not is_browser_active():
        print("Error: No browser detected. Stopping the script.")
        sys.exit(1)
    
    # Start time for the overall timeout
    start_time = time.time()
    
    # Counter to limit the number of tabs (for safety)
    max_tabs = 100
    max_retries = 3  # Maximum retries per tab
    for i in range(max_tabs):
        # Check for maximum execution time
        if time.time() - start_time > max_execution_time:
            print(f"Error: Execution time exceeded ({max_execution_time} seconds). Stopping the script.")
            break
        
        # Select the address bar (Ctrl+L or Cmd+L)
        if os.name == 'nt':  # Windows
            pyautogui.hotkey('ctrl', 'l')
        else:  # macOS/Linux
            pyautogui.hotkey('cmd', 'l')
        
        time.sleep(0.005)  # Adjusted pause for selection
        
        # Try to copy the URL with retries
        url = None
        for attempt in range(max_retries):
            try:
                # Copy the URL (Ctrl+C or Cmd+C)
                if os.name == 'nt':
                    pyautogui.hotkey('ctrl', 'c')
                else:
                    pyautogui.hotkey('cmd', 'c')
                
                time.sleep(0.005)  # Adjusted pause for copying
                
                # Get the URL from the clipboard
                url = pyperclip.paste().strip()
                
                # Verify that the URL is valid
                if url and url.startswith(('http', 'file')):
                    break
                else:
                    print(f"Attempt {attempt + 1}/{max_retries} on tab {i + 1}: Invalid or empty URL, retrying...")
                    time.sleep(0.1)  # Additional pause before retrying
            except Exception as e:
                print(f"Attempt {attempt + 1}/{max_retries} on tab {i + 1}: Error copying URL ({e}), retrying...")
                time.sleep(0.1)
        
        # If no valid URL was obtained after retries
        if not url or not url.startswith(('http', 'file')):
            print(f"Error: Could not obtain a valid URL for tab {i + 1}. Skipping...")
            continue
        
        # If the URL was seen before, stop the loop
        if url in seen_urls:
            print(f"Tab {i + 1}: Repeated URL detected ({url}). Stopping the loop.")
            break
        seen_urls.add(url)
        links.append(url)
        
        # Switch to the next tab (Ctrl+Tab or Cmd+Tab)
        if os.name == 'nt':
            pyautogui.hotkey('ctrl', 'tab')
        else:
            pyautogui.hotkey('cmd', 'tab')
        
        time.sleep(0.005)  # Adjusted pause for tab switching
    
    # Check if any links were saved
    if not links:
        print("Error: No valid links found to save.")
        return
    
    # Save the links to a text file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for link in links:
                f.write(link + '\n')
        print(f"Saved {len(links)} links to {output_file}")
    except Exception as e:
        print(f"Error saving file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        save_open_tabs()
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)