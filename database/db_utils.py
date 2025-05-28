# database/db_utils.py
import json
from .db_config import DBConfig

class DBUtils:
    def save_status(error_message=None):
        status = {"db_error": error_message}
        with open(DBConfig.DB_STATUS_FILE, "w") as f:
            json.dump(status, f)