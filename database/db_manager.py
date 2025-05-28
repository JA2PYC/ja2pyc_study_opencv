# database/db_manager.py
class DBManager:
    _db_client = None

    @classmethod
    def _init_client(cls):
        if cls._db_client is None:
            from .db_client import DBClient

            cls._db_client = DBClient()

    @classmethod
    def get_engine(cls):
        cls._init_client()
        return cls._db_client.get_engine()

    @classmethod
    def get_session(cls):
        cls._init_client()
        return cls._db_client.get_session()

    @classmethod
    def get_db(cls):
        cls._init_client()
        return cls._db_client.get_db()
