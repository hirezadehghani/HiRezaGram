from threading import Thread
import socket
import queue
import time
import yaml
import logging
import sys
from module.contacts import Contacts

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class ClientServer:
    def __init__(self) -> None:
        self.msg_queue = queue.Queue()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_thread = ''
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        self.contacts = Contacts("test", "09xxxxxxxxx")
        self.isAliveProgram = True

    def connect_to_server(self) -> None:
        try:
            self.socket.connect((config['General']['CLIENT_HOST'], config['General']['CLIENT_PORT']))
        except:
            print('Error in connecting to chat server (May be server is off!)')
            exit(1)
            
    def get_menu_choice(self) -> None:
        """
        -------------- menu -----------------
        # contacts list
        # chat list
        # New Chat
        """         
        while(self.isAliveProgram):
            choice = input("""
                        1: Contacts
                        2: Chat List
                        3: New Chat
                        4: login ( in construction :) )
                        5: Register ( in construction :) )
                        6: Quit

                        Please enter your choice: """)
            
            if choice == "1":
                self.show_contacts_menu()
            elif choice == "2":
                self.show_chat_list()
            elif choice == "3":
                self.chat()
            elif choice == "4" or choice == "5":
                print("in construction ... ")
            elif choice=="6":
                self.isAliveProgram = False
                sys.exit
            else:
                print("You must only select either any number from 1 to 6")
                print("Please try again")
                self.get_menu_choice()
    
    def show_contacts_menu(self) -> None:        
        choice = input("""
                      1: Add new contact
                      2: Show contacts
                      3: Search Contacts

                      Please enter your choice: """)

        if choice == "1":
            name = str(input("Please enter name?"))
            phone = str(input("Please enter phone number?"))
            self.contacts = Contacts(name, phone)
            self.get_menu_choice()
            
        elif choice == "2":
            self.contacts.show_contacts()
            self.get_menu_choice()
            
        elif choice == "3":
            self.contacts.search_contacts()
            self.get_menu_choice()
            
        else:
            print("You must only select either any number from 1 to 3")
            print("Please try again")
            self.get_menu_choice()
        
    def chat(self):
        pass
    
    def show_chat_list(self):
        pass        
    
    def handle_data(self) -> None:
        self.queue_thread = Thread(target=self.get_data_from_queue, args=(self.msg_queue,))
        self.queue_thread.start()
                
    def get_data_from_queue(self):
        while True:
            data = input('Enter message: ')
            self.msg_queue.put(data)
            try:
                message = self.msg_queue.get(timeout=0.5)
                byte_message = message.encode(encoding="utf-8")[:1024]
                if message != None:
                    try:
                        self.socket.send(byte_message)
                        server_request = self.socket.recv(1024)
                        server_message = server_request.decode(encoding="utf-8")[:1024]
                        print("", end="\n")
                        print(server_message, end="\n")
                    except socket.error as e:
                        print(f"An error in socket occurred")
                        if isinstance(e.args, tuple):
                            logging.error(f"An error occurred: {e}")
                if message == "q":
                    self.socket.close()
                    break
            except queue.Empty as e:
                print("/|\\", end="\n")
            except TimeoutError as e:
                print("Waiting to insert message")