import os
import tkinter as tk
from tkinter import filedialog

def path():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="select a folder")
    root.destroy()

    if folder_path:
        return folder_path
    else:
        return None
    
def get_files_in_directory_os(path):
    try: 
        entries = os.listdir(path)
        files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]
        return files
    
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
        return []
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
        return []
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return []
    
def get_file_size_from_path(file_path):
    try:
        file_size_bytes = os.path.getsize(file_path)
        print(f"The file size is: {file_size_bytes} bytes")

        file_size_kb = file_size_bytes / 1024
        file_size_mb = file_size_kb / 1024
        file_size_gb = file_size_mb / 1024

        print(f"File Size (KB): {file_size_kb:.2f} KB")
        print(f"File Size (MB): {file_size_mb:.2f} MB")
        print(f"File Size (GB): {file_size_gb:.2f} GB")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access the file '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")