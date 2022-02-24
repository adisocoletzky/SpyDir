from watchdog.observers import Observer
from watchdog.events import *
import time
from client import start_client

flag = True
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        global flag
        flag = False
        if event.is_directory:
            print("directory moved from {0} to {1}".format(event.src_path, event.dest_path))

        else:
            print("file moved from {0} to {1}".format(event.src_path, event.dest_path))

    def on_created(self, event):
        global flag
        flag = False
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        global flag
        flag = False
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        global flag
        flag = not flag
        if flag:
            return
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            msg = "file modified:{0}".format(event.src_path)
            print(msg)
            print('')
            index = msg.index(':')
            path_event_after = msg[index + 1:]
            start_client(path_event_after)


if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler, "E:\cyber_test", True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
