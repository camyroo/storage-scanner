import os
import tkinter as tk
from tkinter import filedialog


def select_folder():
    """Opens a folder selection dialog and returns the selected path"""
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select a folder")
    root.destroy()
    return folder_path if folder_path else None


def get_files_in_directory(path):
    """Returns a list of files (not directories) in the given path"""
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


def get_file_size(file_path):
    """Returns file size in bytes, or None if error occurs"""
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to access the file '{file_path}'.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def format_file_size(size_bytes):
    """Converts bytes to KB, MB, GB and returns a dictionary"""
    if size_bytes is None:
        return None
    
    return {
        'bytes': size_bytes,
        'kb': size_bytes / 1024,
        'mb': size_bytes / 1024 / 1024,
        'gb': size_bytes / 1024 / 1024 / 1024
    }


def print_file_info(file_path):
    """Prints detailed file size information"""
    size_bytes = get_file_size(file_path)
    
    if size_bytes is None:
        return
    
    sizes = format_file_size(size_bytes)
    
    print(f"\nFile: {os.path.basename(file_path)}")
    print(f"The file size is: {sizes['bytes']} bytes")
    print(f"File Size (KB): {sizes['kb']:.2f} KB")
    print(f"File Size (MB): {sizes['mb']:.2f} MB")
    print(f"File Size (GB): {sizes['gb']:.2f} GB")