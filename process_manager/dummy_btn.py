from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import QTimer


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.title = 'Demo'
        self.setGeometry(0,0,900,500)
        self.dummy_btn()
        self.dummy_timer()
        Timer = MyWindow()
        self.layout = QVBoxLayout()
        self.layout.addWidget(Timer)
        window.setLayout(QBoxLayout)
        #self.layout.addWidget(self.dummy_btn)

    
    def dummy_timer(self):
        self.timer = QTimer(self)
        self.timer.setInterval(10000)
        self.timer.start()
        self.timer.timeout.connect(self.update_timer)

    def dummy_btn(self):
        self.btn = QPushButton('Button', self)
        self.btn.move(500,0)

    def update_timer(self):
        print("Timer Triggered")


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()


