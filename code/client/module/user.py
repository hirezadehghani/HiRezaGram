from client.module.contact import Contact
from utils import generate_uuid

class User:
    def __init__(self, username: str, email: str, contacts: dict, status: bool):
        self.user_id = generate_uuid()
        self.username = username
        self.email = email
        self.contacts = contacts
        self.status = status
        
    def get_user_info(self):
        pass