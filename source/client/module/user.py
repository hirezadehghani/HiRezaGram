from module.utils import generate_uuid

class User:
    def __init__(self, username: str, email: str, contacts: dict, status: bool):
        self.user_id = generate_uuid()
        self.username = username
        self.email = email
        self.contacts = contacts
        self.status = status #online offline;
    
    def get_user_id(self) -> str:
        return self.user_id
            
    def get_user_info(self):
        pass