import socket
import time
import threading
import queue

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 1658

def get_input():
    while True:
        data = input()
        queue.put(data)

msg_queue = queue.Queue()
threading.Thread(target = get_input(), args = (msg_queue, ))
input_thread = threading.Thread(target= get_input, args=(msg_queue, ))
input_thread.start()

while True:
    try:
        msg = msg_queue.get(timeout=0.1)
        if msg != None:
            print(msg)
            if msg == "q":
                break
    except queue.Empty as e:
        print("/|\\", end="")
    except TimeoutError as e:
        print("Waiting to insert message")
input_thread.join()

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((SERVER_HOST, SERVER_PORT))