import os
from file_functions import get_files_in_directory, get_folders_in_directory, print_file_info


class Scanner:
    def __init__(self, start_path):
        self.start_path = start_path
        self.scan()

    def scan(self):
        """Scans the directory and prints info for all files"""
        files = get_files_in_directory(self.start_path)
        folders = get_folders_in_directory(self.start_path)

        print(f"\nFound {len(folders)} folders in {self.start_path}")
        print(folders)
        print(f"\nFound {len(files)} files in {self.start_path}")
        print(files)
        
        for file in files:
            full_path = os.path.join(self.start_path, file)
            print_file_info(full_path)