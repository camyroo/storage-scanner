from tkinter import *
from tkinter import ttk 
from select_dir import path

class StorageScan:
    def __init__(self, root):
        self.root = root
        self.root.title("Storage Scanner")
        self.root.geometry("800x600")
        self.folder_var = StringVar(value="No folder selected")
        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self.root, text="Storage Scanner")
        label.pack(pady=20)

        button = ttk.Button(self.root, text="Select Folder", command=self.select_folder)
        button.pack(pady=10)

    def select_folder(self):
        folder_path = path()

        if folder_path:
            self.folder_var.set(f"PATH: {folder_path}")
            self.selected_folder = folder_path


def start_gui(): 
    root = Tk()  
    app = StorageScan(root)
    root.mainloop()

if __name__ == "__main__":
    start_gui()