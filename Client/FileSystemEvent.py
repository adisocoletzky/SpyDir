from watchdog.observers import Observer
from watchdog.events import *
import time
from client_socket import socket_handler
from notifications import Notification


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, base_directory):
        FileSystemEventHandler.__init__(self)
        self.base_directory = base_directory

    def on_created(self, event):
        if event.is_directory:
            socket_handler(event.src_path.replace(self.base_directory, ''), Notification.DIR_CREATED)
        else:
            socket_handler(event.src_path.replace(self.base_directory, ''), Notification.FILE_CREATED)

    def on_deleted(self, event):
        if event.is_directory:
            socket_handler(event.src_path.replace(self.base_directory, ''), Notification.DIR_DELETED)
        else:
            socket_handler(event.src_path.replace(self.base_directory, ''), Notification.FILE_DELETED)

    def on_modified(self, event):
        if event.is_directory:
            # socket_handler(event.src_path.replace(self.base_directory, ''), Notification.DIR_MODIFIED)
            pass
        else:
            socket_handler(event.src_path.replace(self.base_directory, ''), Notification.FILE_MODIFIED)


def start_client(directory_path):
    observer = Observer()
    event_handler = FileEventHandler(directory_path)
    observer.schedule(event_handler, directory_path, True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()