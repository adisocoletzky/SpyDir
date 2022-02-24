import socket
LOCALHOST = '127.0.0.1'
PORT = 1235

def start_client(data):
    client_socket = socket.socket()
    client_socket.connect((LOCALHOST, PORT))
    length=(str(len(data))).zfill(3)
    client_socket.send(length.encode())
    client_socket.send(data.encode())
    client_socket.close()
