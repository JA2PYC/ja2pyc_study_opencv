# utils/logger.py
import datetime

class Logger:
    @staticmethod
    def log(msg):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[Log][{now}] {msg}")
