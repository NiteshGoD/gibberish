import sys
from source.notes_service import NotesService
from source.user_service import UserService
from getpass import getpass


class MainApp():
    """Main starting point of the app
    """
    def __init__(self):
        self.user_service = UserService()
        self.notes_service = NotesService(self.user_service)
        
    def register_prompt(self):
        new_user_name = input("Enter new user name: ")
        new_user_password = getpass("Enterpassword here")
        return new_user_name,new_user_password
    
    def login_prompt(self):
        user_name = input("Enter user name: ")
        user_password = getpass("Enterpassword here: ")
        return user_name, user_password
    
    def note_prompt(self):
        title = input("Input note title")
        note_txt = input("Enter your note here ")
        return title, note_txt
    
    def welcome_screen(self):
        print("1. Press 1 to register user ")
        print("2. press 2 to login")
        running = True
        user_input = input("Enter your choice here")
        while running:
            if user_input == "quit":
                running = False
                sys.exit()
            else:
                if user_input == "1":
                    new_user_name, new_user_password = self.register_prompt()
                    self.user_service.register_new_user(new_user_name,new_user_password)
                    self.welcome_screen()
                
                elif user_input == "2":
                    user_name, password = self.login_prompt()
                    print(self.user_service.login_user(user_name,password))
                    if self.user_service.logged_in_user:
                        #prompt for note entry
                        title, note_txt = self.note_prompt()
                        self.notes_service.save_new_entry(self.user_service.logged_in_user.name, note_txt)
                        self.welcome_screen()
                        
                    
                    
if __name__ == "__main__":
    main_app = MainApp()
    main_app.welcome_screen()
            
            