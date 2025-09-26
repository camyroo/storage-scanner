from tkinter import *
from tkinter import ttk 
from file_functions import path
from Log import Logger 

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Storage Scanner")
        self.root.geometry("800x600")
        self.folder_var = StringVar(value="No folder selected")
        self.selected_folder = None
        


        self.use_debug = BooleanVar(value=True)
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10) 

        self.main_tab()
        self.results_tab()
        self.analysis_tab()
        self.advanced_tab()
        self.test_tab()

    def main_tab(self):
        main_frame = ttk.Frame(self.notebook)
        self.notebook.add(main_frame, text="Main")

        container = ttk.Frame(main_frame)
        container.grid(row=0, column=0, sticky="ew")
        main_frame.columnconfigure(0, weight=1)  

        ttk.Label(container, text="Choose Directory to Search: ").grid(row=0, column=0, sticky="W")
        ttk.Button(container, text="Browse", command=self.select_folder).grid(row=0, column=1, padx=30)
        ttk.Label(container, textvariable=self.folder_var, wraplength=300).grid(row=0, column=2, sticky="W")
        ttk.Button(container, text="Run", command=self.start_scan).grid(row=10, column=1)

        container.columnconfigure(0, weight=0)  
        container.columnconfigure(1, weight=0)    
        container.columnconfigure(2, weight=1)

    def results_tab(self):
        results_frame = ttk.Frame(self.notebook)
        self.notebook.add(results_frame, text="Results")

    def analysis_tab(self):
        analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(analysis_frame, text="Analysis")

    def advanced_tab(self):
        advanced_frame = ttk.Frame(self.notebook)
        self.notebook.add(advanced_frame, text="Advanced")

        container = ttk.Frame(advanced_frame)
        container.grid(row=0, column=0, sticky="ew")

        ttk.Checkbutton(container, text="Enable Debug", variable=self.use_debug).grid(row=0, column=1)

    def test_tab(self):
        test_frame = ttk.Frame(self.notebook)
        self.notebook.add(test_frame, text="Test")

        container = ttk.Frame(test_frame)
        container.grid(row=0, column=0, sticky="ew")

        ttk.Button(container, text="Test log", command=self.test).grid(row=10, column=1)


    def select_folder(self):
        folder_path = path()

        if folder_path:
            self.folder_var.set(f"PATH: {folder_path}")
            self.selected_folder = folder_path

    def start_scan(self):
        if self.selected_folder:
            from os_functions import os_functions
            os_functions(self.selected_folder)

            

            if self.use_debug.get():
                print(f"Beginning Scan: {self.selected_folder}")

    def test(self):
        Logger(self.use_debug.get())



def start_gui(): 
    root = Tk()  
    app = GUI(root)
    root.mainloop()

if __name__ == "__main__":
    start_gui()