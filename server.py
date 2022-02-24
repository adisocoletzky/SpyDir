import socket
import threading
from Comparefiles import comparefiles
from schedule_tasks import set_source, set_destination, start_thread_backup, get_from_backup
LOCALHOST = '127.0.0.1'
PORT = 1235


set_source(r"E:\cyber_test")
set_destination(r"E:\cyber_test_backup")
start_thread_backup()
def start_server() -> None:
    server_socket = None
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((LOCALHOST, PORT))
        server_socket.listen(5)
        while True:
            client_socket, address = server_socket.accept()
            threading.Thread(target=conn_with_client, args=[client_socket]).start()

    except:
        if server_socket:
            server_socket.close()
        import traceback
        traceback.print_exc()

def conn_with_client(client_socket: socket.socket) -> None:
    try:
        # while True:
        request = client_socket.recv(3)
        length=int(request.decode())
        data=client_socket.recv(length).decode() #the path after event
        path_event_before = get_from_backup(data, "E:\cyber_test_backup")
        comparefiles(data, path_event_before)
    except:
        try:
            if client_socket:
                client_socket.close()
        except:
            pass
start_server()