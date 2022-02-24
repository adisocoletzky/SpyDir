from threading import Thread

import schedule
import time
from shutil import copytree, rmtree
import os
from datetime import datetime

SOURCE_DIR = ''
DESTINATION_DIR = ''


def backup_dir(src: str, dest: str) -> None:
    try:
        copytree(src, dest)
    except FileExistsError:
        # In case destination directory have already existed - remove dir and try again
        rmtree(dest)
        copytree(src, dest)
    except FileNotFoundError:
        # In case source directory does not exist - create empty destination dir
        if not os.path.exists(dest):
            os.mkdir(dest)
    finally:
        print(f'{src} backup created successfully in {dest} | Date: {datetime.now()}')


def get_from_backup(modified_path, dest):
    last_slash = max(modified_path.rfind("\\"), modified_path.rfind("/"))
    absolute_path = modified_path[last_slash + 1:]
    backup_path = dest + "\\" + absolute_path
    return backup_path


def start_backup():
    schedule.every(5).seconds.do(lambda: backup_dir(SOURCE_DIR, DESTINATION_DIR))
    while True:
        schedule.run_pending()
        time.sleep(0.1)


def start_thread_backup():
    thread = Thread(target=start_backup)
    thread.start()


def set_source(src):
    global SOURCE_DIR
    SOURCE_DIR = src


def set_destination(dest):
    global DESTINATION_DIR
    DESTINATION_DIR = dest
