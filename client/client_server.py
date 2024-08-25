from threading import Thread
import socket
import queue
import time
import yaml
import logging

# with open('../config.yaml', 'r') as file:
#     config = yaml.safe_load(file)

class ClientServer:
    def __init__(self) -> None:
        self.msg_queue = queue.Queue()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.input_thread = ''
        logging.basicConfig(filename='error.log', level=logging.ERROR)

    def connect_to_server(self) -> None:
        try:
            self.socket.connect(("127.0.0.1", 1658))
        except:
            print('Error in connecting to chat server (May be server is off!)')
            exit(1)
    
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
                        print(server_message, end="\n")
                    except socket.error as e:
                        print(f"An error in socket occurred")
                        if isinstance(e.args, tuple):
                            logging.error(f"An error occurred: {e}")
                            if (hasattr(e, [0]) and [0] == e.PIPE):
                                print("An error in detecting remote disconnection")
                if message == "q":
                    self.socket.close()
                    break
            except queue.Empty as e:
                print("/|\\", end="\n")
            except TimeoutError as e:
                print("Waiting to insert message")