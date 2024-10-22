from client_server import ClientServer

if __name__ == "__main__":
    print('in client')
    
    client_server = ClientServer()
    client_server.connect_to_server()
    client_server.get_menu_choice()