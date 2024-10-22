from code.utils import generate_uuid

class Contact:
    def __init__(self, contact_id: int, name: str, phone: str, user_id: str):
        # create new contacts dictionary
        self.contact_id = generate_uuid()
        self.contacts = dict()
        self.last_message_time = None
        self.status = None
        self.user_id = user_id
        
        self.add_new_contact(name, phone)
        
    def add_new_contact(self, name:str, phone:str) -> None:
        
        self.contacts[name] = phone
        print(f"{name, self.contacts[name]} added to contacts")

    def show_contacts(self) -> dict:
        print(self.contacts.values())

    def search_contacts(self) -> dict:
        name = input("Enter contact name: ")
        if name in self.contacts:
            print(f" Found Contact: {name} => {self.contacts.get(name)}")
        else:
            print("Contact is not found!")