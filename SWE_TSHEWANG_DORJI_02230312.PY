import os
import time

# List of file paths you want to open
file_paths = [
    r"C:\Users\Damchey\Documents",
    r"C:\Users\Damchey\OneDrive\Pictures\Screenshots",
    r"C:\Users\Damchey\Downloads\Telegram Desktop"
]

# Iterate through the list of file paths
for file_path in file_paths:
    try:
        # Open the folder using the default file explorer
        os.startfile(file_path)
        print(f"Opened: {file_path}")
    except Exception as e:
        # Handle any exceptions that might occur while opening the folder
        print(f"Error opening {file_path}: {e}")

    # Pause for 10 seconds (adjust this duration as needed)
    time.sleep(10)

# End of the loop
print("All folders have been opened.")