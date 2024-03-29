from typing import Optional
from source.model import User
from source import DataRepository


class UserService():
    """Handles User CRUD"""

    def __init__(self, logged_in_user : Optional[User] = None ):
        self.data_repo = DataRepository()
        self.logged_in_user = logged_in_user

    def register_new_user(self, user_name: str, password: str):
        try:
            self.data_repo.add_user(user_name=user_name, password=password)
        except Exception as ex:
            raise ex
        new_user = self.data_repo.get_user(
            user_name=user_name, password=password)
        return new_user

    def get_registered_user(self, user_name, password):
        return self.data_repo.get_user(user_name=user_name, password=password)
    
    def login_user(self, user_name, password):
        user = self.get_registered_user(user_name, password)
        if not user:
            raise Exception("No such user's found!!!")
        self.logged_in_user = user
        return self.logged_in_user
