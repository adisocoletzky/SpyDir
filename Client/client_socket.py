import os
import socket

from generator import get_id
from notifications import Notification

SERVER_ADDRESS = '127.0.0.1'
PORT = 1234

client_socket = None

BASE_DIRECTORY = ''


def connect(base_directory, zip_path):
    global client_socket
    global BASE_DIRECTORY
    try:
        client_socket = socket.socket()
        client_socket.connect((SERVER_ADDRESS, PORT))
        BASE_DIRECTORY = base_directory
        socket_handler(zip_path, Notification.ZIP_INIT)
    except:
        if client_socket:
            client_socket.close()


def socket_handler(path, notification):
    global client_socket
    global BASE_DIRECTORY
    data = str(notification.value).encode()

    if notification == Notification.ZIP_INIT:
        data += get_id(8).encode() + open(path, mode='rb').read()
        os.remove(path)

    elif notification == Notification.FILE_MODIFIED:
        data += path.encode() + b'|' + open(BASE_DIRECTORY + path, mode='rb').read()

    else:  # Notification.FILE_CREATED | Notification.DIR_CREATED | Notification.FILE_DELETED | Notification.DIR_DELETED
        data += path.encode()

    length = (str(len(data))).zfill(8)
    client_socket.send(length.encode())
    client_socket.send(data)
