import socket
from threading import Thread, Lock
from typing import Dict
import yaml
import configparser

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class ChatServer:
    def __init__(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_host = config['General']['SERVER_HOST']
        self.server_port = config['General']['SERVER_PORT']
        self.socket.bind((self.server_host, self.server_port))
        self.connections:Dict[str, socket.socket] = {}
        self.connection_lock = Lock()

    def listen(self)->None:
        self.socket.listen()

    def accept_connections(self)->None:
        while True:
            conn, addr = self.socket.accept()
            print(f"client {addr} is connected")
            approve_message = (f"Server approved: Welcome {addr}")
            # self.socket.send(approve_message)
            print(approve_message)
            thread = Thread(target = self.handle_connection, args = (conn, addr))
            thread.start()

    def handle_connection(self, client_socket:socket, source_addr):
        while True:
            request = client_socket.recv(1024)
            self.broadcast(source_addr, request)
            if (request == 'q'):
                print(f"client {source_addr} is disconnected")
                self.shutdown()
    
    def broadcast(self, source_addr: str, data:bytes):
        for addr, conn in self.connections.items():
            if addr != source_addr:
                conn.sendall(f"{source_addr}: {data}".encode(encoding="utf-8"))

    def shutdown(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()