# database/database_client.py
import threading

# SQL Alchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

# Abstract Class
from .abstract_db_client import AbstractDBClient

# Settings
from .db_config import DBConfig
from .db_utils import DBUtils


class DBClient(AbstractDBClient):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                cls._instance = super().__new__(cls)
                cls._instance._init_db_client()
        return cls._instance

    def _init_db_client(self):
        try:
            self._create_db_if_not_exists()
            self.engine = create_engine(DBConfig.DATABASE_URL, pool_pre_ping=True)
            self.SessionLocal = sessionmaker(
                bind=self.engine, autocommit=False, autoflush=False
            )
            DBUtils.save_status(None)
        except OperationalError as e:
            DBUtils.save_status(f"[Error] Fail : _init_db_client : {e}")
            self.engine = None
            self.SessionLocal = None

    def _create_db_if_not_exists(self):
        try:
            engine = create_engine(DBConfig.DATABASE_URL_DEFAULT)
            with engine.connect() as conn:
                db_name = DBConfig.DB_NAME
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {db_name}"))
                conn.commit()
        except OperationalError as e:
            DBUtils.save_status(f"[Error] Fail : _create_db_if_not_exists : {e}")

    def get_session(self):
        return self.SessionLocal()

    def get_engine(self):
        return self.engine

    def get_db(self):
        db = self.get_session()
        try:
            yield db
        finally:
            db.close()
