import socket
from threading import Thread, Lock
from typing import Dict
import yaml
import configparser
import logging
import time

with open('../config.yaml', 'r') as file:
    config = yaml.safe_load(file)

class ChatServer:
    def __init__(self) -> None:
        logging.basicConfig(filename='error.log', level=logging.ERROR)
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((config['General']['CLIENT_HOST'], config['General']['CLIENT_PORT']))
            self.connect_to_socket()
        except Exception as e:
            print('Error: can not connect to socket')
            logging.error(f"An error occurred: {e}")
        self.connections:Dict[str, socket.socket] = {}
        self.connection_lock = Lock()

    def connect_to_socket(self):        
        self.socket.listen()
        print(f"Listening on {(config['General']['CLIENT_HOST'], config['General']['CLIENT_PORT'])}")

    def accept_connections(self):
        while True:
            client_socket, addr = self.socket.accept()
            self.connections[addr] = client_socket
            print(f"client {addr} is connected")
            client_socket.send(f"Server approved: Welcome {addr}".encode("utf-8"))
            handle_message_thread = Thread(target = self.handle_client, args = (client_socket, addr))
            handle_message_thread.start()

    def handle_client(self, client_socket:socket, addr):
        try:
            while True:
                request = client_socket.recv(1024).decode("utf-8")
                if(request.lower() == "q"):
                    client_socket.send("your connection is closed".encode("utf-8"))
                    client_socket.close()
                    self.connections.pop(addr)
                    print(f"connection to client ({addr}) closed")
                    break
                print(f"Received from {addr}: {request}\n")
                client_socket.send(f"Your message accepted".encode("utf-8"))
                self.broadcast(addr, request)
        except Exception as e:
            print('Error: can not handle client connection')
            logging.error(f"An error occurred: {e}")

    def broadcast(self, source_addr: str, data:bytes):
        try:
            for addr, conn in self.connections.items():
                if addr != source_addr:
                    conn.sendall(f"{source_addr}: {data}".encode(encoding="utf-8"))
        except socket.error as e:
            print(f"An error in socket occurred")
            if isinstance(e.args, tuple):
                logging.error(f"An error occurred: {e}")
                if e[0] == e.PIPE:
                    print("An error in detecting remote disconnection")