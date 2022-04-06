from FileSystemEvent import start_client
import tkinter.filedialog as FileDialog

from zip_compressor import compress_dir
from client_socket import connect

PATH = FileDialog.askdirectory()
ZIP_PATH = PATH + r'\dir.zip'
compress_dir(PATH, ZIP_PATH)

connect(PATH, ZIP_PATH)
start_client(PATH)
