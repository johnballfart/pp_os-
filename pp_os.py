import os
import subprocess
import tkinter as tk
from tkinter import messagebox, simpledialog

# Path to the Desktop
DESKTOP_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

def execute_command(command):
    """Process user commands."""
    if command.startswith("pp/"):
        # Open an app
        app_path = command[3:].strip()
        full_path = os.path.join(DESKTOP_PATH, app_path)
        if os.path.exists(full_path):
            try:
                subprocess.Popen(["open", full_path])
                output_label.config(text=f"Opened: {app_path}")
            except Exception as e:
                output_label.config(text=f"Error opening app: {e}")
        else:
            output_label.config(text="File not found on Desktop.")
    elif command.startswith("poopoo/"):
        # Close an app
        app_path = command[7:].strip()
        try:
            subprocess.run(["pkill", "-f", app_path])
            output_label.config(text=f"Closed: {app_path}")
        except Exception as e:
            output_label.config(text=f"Error closing app: {e}")
    elif command.startswith("caca/"):
        # Rename a file
        app_path = command[5:].strip()
        full_path = os.path.join(DESKTOP_PATH, app_path)
        if os.path.exists(full_path):
            new_name = simpledialog.askstring("Rename File", "What do you want to rename this file?")
            if new_name:
                new_path = os.path.join(DESKTOP_PATH, new_name)
                os.rename(full_path, new_path)
                output_label.config(text=f"Renamed to: {new_name}")
            else:
                output_label.config(text="Rename canceled.")
        else:
            output_label.config(text="File not found on Desktop.")
    elif command.startswith("cheeks/"):
        # Create a new folder
        folder_name = "New Folder"
        folder_path = os.path.join(DESKTOP_PATH, folder_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
            output_label.config(text=f"Folder created: {folder_name}")
        except Exception as e:
            output_label.config(text=f"Error creating folder: {e}")
    elif command == "close/":
        # Close the app
        root.destroy()
    else:
        output_label.config(text="Unknown command.")

# Create the GUI
root = tk.Tk()
root.title("pp os")
root.geometry("600x400")

# Welcome message
welcome_label = tk.Label(root, text="welcome to pp os!!!!!", font=("Courier", 16), fg="blue")
welcome_label.pack(pady=20)

# Input box
entry = tk.Entry(root, font=("Courier", 14), width=50)
entry.pack(pady=10)

# Output message
output_label = tk.Label(root, text="", font=("Courier", 12), fg="green")
output_label.pack(pady=20)

# Submit button
def on_submit():
    command = entry.get()
    execute_command(command)
    entry.delete(0, tk.END)

submit_button = tk.Button(root, text="Submit", font=("Courier", 14), command=on_submit)
submit_button.pack(pady=10)

root.mainloop()