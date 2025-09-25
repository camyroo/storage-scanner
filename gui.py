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

        ttk.Label(self.root, text="Choose Directory to Search: ").grid(row=1, column=1)
        ttk.Button(self.root, text="Select Folder", command=self.select_folder).grid(row=1, column=2)

        ttk.Label(self.root, textvariable=self.folder_var).grid(row=1, column=3, sticky="E")

        for child in self.root.winfo_children():
            child.grid_configure(padx=5, pady=5)

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