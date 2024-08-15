from chat_server import ChatServer

HOST = "127.0.0.1"
PORT = 1658

if __name__ == "__main__":
    print("in server")

    chat_server = ChatServer()
    chat_server.listen()
    chat_server.accept_connections()