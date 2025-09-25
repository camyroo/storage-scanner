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