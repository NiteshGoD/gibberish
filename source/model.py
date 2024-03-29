"""Data Model"""
from typing import Optional
from dataclasses import dataclass
from collections import namedtuple


@dataclass
class User:
    __field_lst__ = ['name', 'password', 'key']
    name: str
    password: str
    key: str

    def get_user_info(self):
        Person = namedtuple("Person", ["name", "password", "key"])
        return Person(self.name, self.password, self.key)


@dataclass
class Note:
    date_time: str
    note_txt: str
    author: str
    title: Optional[str] = "title_here"
    
    def get_note_info(self):
        Note_data = namedtuple("Note_data",["date_time","title","note_txt", "author"])
        return Note_data(self.date_time,self.title,self.note_txt, self.author)
    
# Person = namedtuple("Person",["name","password"])

# if __name__ =="__main__":
#     user = User("Gopal","Password","thisiskey")
#     user_name, user_password, user_key = user.get_user_info()
#     print(user_name, user_password, user_key)
#     print(user.__field_lst__)
