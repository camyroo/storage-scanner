import os

from select_dir import path


# def scan_directory(path):

def main():
    folder_path = path()

    if folder_path:
        print(f"PATH: {folder_path}")
    else:
        print("No folder selected")
    
if __name__ == "__main__":
    main()