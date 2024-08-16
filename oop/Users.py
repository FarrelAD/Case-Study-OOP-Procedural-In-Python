from User import User

class Users:
    def __init__(self) -> None:
        self.users_data = []
    
    def add_user(self, name, email, date_of_birth):
        self.users_data.append(User(name, email, date_of_birth))