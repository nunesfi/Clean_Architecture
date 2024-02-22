from abc import ABC, abstractclassmethod
from typing import List
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractclassmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass

    @abstractclassmethod
    def select_user(self, first_name: str) -> List[Users]: pass
    
