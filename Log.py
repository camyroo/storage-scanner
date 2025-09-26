import os
from datetime import datetime

class Logger:
    def __init__(self, use_debug: bool, log_file: str = "Storage_Scan.log"):
        self.use_debug = use_debug
        self.log_file = log_file

        self.init_logs()

    def init_logs(self):
        # searches for existing log file, if not creates one
        if os.path.exists(self.log_file): return
        
        with open(self.log_file, "x") as f:
                f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} Initialized Log!")

        self.debug("Log initialized")
        
        
    def debug(self, message: str):
        if not self.use_debug: return 
        
        print(f"DEBUG: {message}")
        
    # def info(self, message: str):
    # def warning(self, message: str):
    # def error(self, message: str):

