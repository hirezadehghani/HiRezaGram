class Contacts:
    def __init__(self):
        self.contacts = dict()

    def add_new_contact(self, name:str, phone:str) -> None:
        self.contacts[name] =  phone

    def show_contacts(self) -> dict:
        print(self.contacts.values())

    def search_contacts(self) -> dict:
        name = input()
        if name in self.contacts:
            print(self.contacts.get(name))