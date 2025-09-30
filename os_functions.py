import os

class os_functions:
    def __init__(self, selected_path):
        self.start_path = selected_path 
        self.current_path = selected_path 

        self.start(self.start_path)

    def start(self, path=None):
        files = self.get_files_in_directory_os(self.start_path)
        for file in files: 
            full_path = os.path.join(path, file)
            self.get_file_size_from_path(full_path) 

    def get_files_in_directory_os(self, path=None):
        directory_path = path if path is not None else self.start_path
        
        try: 
            entries = os.listdir(directory_path)
            files = [entry for entry in entries if os.path.isfile(os.path.join(directory_path, entry))]
            print(files)


            return files
        
        except FileNotFoundError:
            print(f"Error: Directory '{directory_path}' not found.")
            return []
        except NotADirectoryError:
            print(f"Error: '{directory_path}' is not a directory.")
            return []
        except PermissionError:
            print(f"Error: Permission denied to access '{directory_path}'.")
            return []
        
    def get_file_size_from_path(self, file_path):
        try:
            file_size_bytes = os.path.getsize(file_path)
            print(f"\nFile: {os.path.basename(file_path)}")
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