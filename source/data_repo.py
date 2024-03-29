"""This is the Data Repositories
    Data will be saved in the files 
    
    For now the data will be saved in txt files
    
    """
from typing import List
from cryptography.fernet import Fernet
from .model import User, Note


class DataRepository():
    """Read and write operations on file"""

    def __init__(self, user_file_path="users.txt", notes_file_path="notes.txt"):
        """initialize file path and check for the required files"""
        self.user_file = user_file_path
        self.notes_file = notes_file_path

    def _get_user_info_from_file(self):
        """Reads lines from the txt file and returns list of strings"""
        with open(self.user_file, "r") as f_name:
            lines = f_name.readlines()
        return lines
    
    def _get_notes_info_from_file(self):
        """Reads lines from the txt file and returns list of strings"""
        with open(self.notes_file, "r") as f_name:
            lines = f_name.readlines()
        return lines

    def get_users(self):
        """gets the list of username and password from the file
        return: List[User]
        """
        user_infos_from_file = self._get_user_info_from_file()
        users: List[User] = []
        for user_infos in user_infos_from_file:
            user_name, password, key, *others = user_infos.split(" ")
            users.append(User(name=user_name, password=password, key=key))
        return users

    def add_user(self, user_name, password, key=Fernet.generate_key()):
        """writes the new user and password in the file"""
        user = User(name=user_name, password=password, key=key.decode())
        line_to_write = " ".join(user.get_user_info())
        with open(self.user_file, "a") as f_name:
            f_name.write(line_to_write + "\n")
        return line_to_write

    def save_notes(self, note: Note):
        """Writes the notes in the txt file"""
        with open(self.notes_file,"a") as f_name:
            to_save = "::".join(note.get_note_info()) +"\n"
            f_name.write(to_save)
        return to_save

    def get_user(self, user_name: str, password: str):
        stored_users = self.get_users()
        for user in stored_users:
            if user.name == user_name and user.password == password :
                return user
        return
    
    def get_notes(self):
        """gets the list of username and password from the file
        return: List[User]
        """
        notes_infos_from_file = self._get_notes_info_from_file()
        notes: List[Note] = []
        for notes_infos in notes_infos_from_file:
            date_time, note_txt, author, *others = notes_infos.split("::")
            notes.append(Note(date_time=date_time, note_txt=note_txt, author=author))
        return notes

    def remove_user(self):
        """Removes user from the file"""
        raise NotImplementedError

    def add_note(self):
        """writes the notes in a file"""
        raise NotImplementedError

    def remove_note(self):
        """Removes the note from the file"""
        raise NotImplementedError
