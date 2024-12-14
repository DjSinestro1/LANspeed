import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def measure_transfer_speed(source, destination):
    # Ensure the source directory exists
    if not os.path.isdir(source):
        messagebox.showerror("Error", f"Source directory '{source}' does not exist.")
        return

    # Ensure the destination directory exists
    if not os.path.isdir(destination):
        messagebox.showerror("Error", f"Destination directory '{destination}' does not exist.")
        return

    # Get list of files in the source directory
    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    
    if not files:
        messagebox.showinfo("Info", "No files to transfer in the source directory.")
        return

    total_size = 0
    start_time = time.time()

    # Copy each file from source to destination and calculate total size
    for file_name in files:
        src_file = os.path.join(source, file_name)
        dest_file = os.path.join(destination, file_name)
        
        shutil.copy2(src_file, dest_file)
        total_size += os.path.getsize(dest_file)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate speed in MB/s
    speed_mbps = (total_size / (1024 * 1024)) / elapsed_time

    messagebox.showinfo("Transfer Complete", f"Transfer completed in {elapsed_time:.2f} seconds.\nSpeed: {speed_mbps:.2f} MB/s")

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        source_entry.delete(0, tk.END)
        source_entry.insert(0, folder_selected)

def select_destination_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        destination_entry.delete(0, tk.END)
        destination_entry.insert(0, folder_selected)

# Create main window
root = tk.Tk()
root.title("File Transfer Speed Test")

# Source folder selection
tk.Label(root, text="Select Source Folder:").grid(row=0, column=0, padx=5, pady=5)
source_entry = tk.Entry(root, width=50)
source_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=5, pady=5)

# Destination folder selection
tk.Label(root, text="Select Destination Folder:").grid(row=1, column=0, padx=5, pady=5)
destination_entry = tk.Entry(root, width=50)
destination_entry.grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_destination_folder).grid(row=1, column=2, padx=5, pady=5)

# Start test button
tk.Button(root, text="Start Test", command=lambda: measure_transfer_speed(source_entry.get(), destination_entry.get())).grid(row=2, columnspan=3, pady=10)

# Run the application
root.mainloop()
