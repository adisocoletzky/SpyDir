import datetime
import shutil
import socket
import threading
import traceback

from Logs import *
from compare_file import compare_files
from notifications import Notification
import os

from zip_extractor import extract_zip

SERVER_ADDRESS = '127.0.0.1'
PORT = 1234

BASE_DIRECTORY = r''  # Fill here you base directory


def start_server() -> None:
    server_socket = None
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((SERVER_ADDRESS, PORT))
        server_socket.listen(5)
        while True:
            client_socket, address = server_socket.accept()
            threading.Thread(target=conn_with_client, args=[client_socket]).start()

    except:
        if server_socket:
            server_socket.close()


def conn_with_client(client_socket: socket.socket) -> None:
    try:
        # Initialization
        user_id = -100000000
        user_directory = ''
        notification = Notification.ZIP_INIT
        time = datetime.datetime.now()

        while True:
            length = client_socket.recv(8)
            length = int(length.decode())
            all_data = client_socket.recv(length)
            notification = Notification(int(all_data[0:1]))
            time = datetime.datetime.now()
            if notification == Notification.ZIP_INIT:
                user_id = int(all_data[1:9])
                zip_content = all_data[9:]
                zip_path = BASE_DIRECTORY + f'\\temp{user_id}.zip'
                user_directory = BASE_DIRECTORY + f'\\{user_id}'
                with open(zip_path, 'wb') as zip_file:
                    zip_file.write(zip_content)
                extract_zip(zip_path, user_directory)
                os.remove(zip_path)
                info_log = InfoLog(user_id, notification, user_directory, time)

            elif notification == Notification.FILE_CREATED:
                relative_path = all_data[1:].decode()
                open(user_directory + relative_path, 'x')
                info_log = InfoLog(user_id, notification, relative_path, time)

            elif notification == Notification.DIR_CREATED:
                relative_path = all_data[1:].decode()
                os.mkdir(user_directory + relative_path)
                info_log = InfoLog(user_id, notification, relative_path, time)

            elif notification == Notification.FILE_DELETED:
                relative_path = all_data[1:].decode()
                os.remove(user_directory + relative_path)
                info_log = InfoLog(user_id, notification, relative_path, time)

            elif notification == Notification.DIR_DELETED:
                relative_path = all_data[1:].decode()
                shutil.rmtree(user_directory + relative_path)
                info_log = InfoLog(user_id, notification, relative_path, time)

            elif notification == Notification.FILE_MODIFIED:
                separator_index = all_data.find(b'|')
                relative_path = all_data[1:separator_index].decode()
                content = all_data[separator_index + 1:]

                before = open(user_directory + relative_path, 'r').read()
                after = content.decode()
                delta = compare_files(before, after)
                with open(user_directory + relative_path, 'wb') as f:
                    f.write(content)
                info_log = InfoLog(user_id, notification, relative_path, time, delta)
            else:
                raise ConnectionError()
            info_log.log()
    except:
        message = traceback.format_exc()
        critical_log = CriticalLog(user_id, notification, time, message)
        critical_log.log()
        if client_socket:
            client_socket.close()


if __name__ == '__main__':
    start_server()
