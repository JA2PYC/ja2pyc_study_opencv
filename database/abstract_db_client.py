#database/abstract_database_client.py
from abc import ABC, abstractmethod

class AbstractDBClient(ABC):
    @abstractmethod
    def get_session(self):
        pass
    
    @abstractmethod
    def get_db(self):
        pass