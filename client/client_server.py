from threading import Thread
import socket
import queue
import time
import yaml

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class ClientServer:
    def __init__(self) -> None:
        self.msg_queue = queue.Queue(time)

    def connect_to_server(self) -> None:
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((config['General']['CLIENT_HOST'], config['General']['CLIENT_PORT']))
        except:
            print('Error in connecting to chat server (May be server is off!)')
            exit(1)

    def get_input(self, queue:queue.Queue, data) -> None:
        while True:
            queue.put(data)
    
    def handle_data(self) -> None:
        data = input()
        self.input_thread = Thread(target=self.get_input, args=(self.msg_queue,data))
        self.input_thread.start()
        self.get_data_from_queue(self.msg_queue)

    def get_data_from_queue(self, msg_queue: queue):
        socket_connection = self.socket

        while True:
            try:
                msg = msg_queue.get(timeout=0.3)
                if msg != None:
                    sending_data = msg.encode(encoding="utf-8")
                    self.socket.sendall(sending_data)
                    data = socket_connection.recv(1024)
                    print(f"Received {data!r}")                
                    if msg == "q":
                        break
            except queue.Empty as e:
                print("/|\\", end="")
            except TimeoutError as e:
                print("Waiting to insert message")
        self.input_thread.join()

        socket_connection.close()