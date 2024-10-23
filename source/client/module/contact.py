from module.utils import generate_uuid

class Contact:
    def __init__(self):
        # create new contacts dictionary
        self.contacts = dict()        
        
    def add_new_contact(self, name: str, phone: str, user_id: str) -> None:
        self.contact_id = generate_uuid()
        self.last_message_time = None
        self.status = None #online or offline
        self.user_id = user_id

        self.contacts[name] = phone
        print(f"{name, self.contacts[name]} added to contacts")

    def show_contacts(self) -> dict:
        for name, phone in self.contacts.items():
            print(f"{name} => {phone}", sep="\n")

    def search_contacts(self) -> dict:
        name = input("Enter contact name: ")
        if name in self.contacts:
            print(f" Found Contact: {name} => {self.contacts.get(name)}")
        else:
            print("Contact is not found!")