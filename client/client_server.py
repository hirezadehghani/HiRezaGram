from threading import Thread
import socket
import queue
import time
import yaml

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class ClientServer:
    def __init__(self) -> None:
        self.msg_queue = queue.Queue()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self) -> None:
        try:
            self.socket.connect((config['General']['CLIENT_HOST'], config['General']['CLIENT_PORT']))
            print(self.socket.recv(1024))
        except:
            print('Error in connecting to chat server (May be server is off!)')
            exit(1)
    
    def handle_data(self) -> None:
        def get_input(queue:queue.Queue):
            while True:
                data = input('Enter message: ')
                sending_data = data.encode(encoding="utf-8")[:1024]
                queue.put(sending_data)

        self.input_thread = Thread(target=get_input, args=(self.msg_queue,))
        self.input_thread.start()
        self.get_data_from_queue(self.msg_queue)

    def get_data_from_queue(self, msg_queue: queue):
        while True:
            try:
                msg = msg_queue.get()
                if msg != None:
                    self.socket.send(msg_queue)
                    if msg == "q":
                        break
            except queue.Empty as e:
                print("/|\\", end="")
            except TimeoutError as e:
                print("Waiting to insert message")
        self.input_thread.join()

        self.socket.close()