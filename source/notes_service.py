"""CRUD on NOtes

    Raises:
        NotImplementedError: _description_
    """
from datetime import datetime
from source import DataRepository
from source.user_service import UserService
from source.model import Note
from source.txt_encryption import Encryptor


class NotesService():
    """Service to register login user and """

    def __init__(self, user_service : UserService):
        self.data_repo = DataRepository()
        self.user_service = user_service

    def save_new_entry(self, user_name: str, note_txt: str):
        """Saves new entry"""
        if self.user_service.logged_in_user:
            date_time = datetime.now().isoformat()
            encryptor = Encryptor(self.user_service.logged_in_user.key.encode())
            note_to_save = Note(date_time=date_time,
                                note_txt=encryptor.encrypt_txt(note_txt), author=user_name)
            return self.data_repo.save_notes(note_to_save)
        raise Exception("No Logged in Users found")

    def get_all_user_entries(self):
        """gets all the user's entry

        Raises:
            NotImplementedError: _description_
        """

        raise NotImplementedError
