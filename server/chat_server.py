import socket
from threading import Thread, Lock
from typing import Dict

class ChatServer:
    def __init__(self, host:str="127.0.0.1", port:int=1658) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.connections:Dict[str, socket.socket] = {}
        self.connection_lock = Lock()

    def listen(self)->None:
        self.socket.listen()

    def accept_connections(self)->None:
        while True:
            conn, addr = self.socket.accept()
            with self.connection_lock:
                self.connections[addr] = conn
            print(f"client {addr} is connected")
            thread = Thread(target = self.handle_connection, args = (conn, addr))
            thread.start()

    def handle_connection(self, client_connection:socket, source_addr):
        while True:
            data = client_connection.recv(1024)
            print(f"{source_addr}: {data.decode()}")
            self.broadcast(source_addr, data)
    # client_connection.close()
    
    def broadcast(self, source_addr: str, data:bytes):
        for addr, conn in self.connections.items():
            if addr != source_addr:
                conn.sendall(f"{source_addr}: {data}".encode())