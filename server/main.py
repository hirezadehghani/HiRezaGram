from chat_server import ChatServer

if __name__ == "__main__":
    print("in server")

    chat_server = ChatServer()
    chat_server.accept_connections()