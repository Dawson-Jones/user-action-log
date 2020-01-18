# from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from QtUi import Ui_MainWindow
from PyQt5.Qt import *
import sys

class WriteThread(QThread):
    _signal = pyqtSignal(str)

    def __init__(self):
        super(WriteThread, self).__init__()

    def run(self):
        self._signal.emit("write OK")

    def callback(self, msg):
        print('callback')


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_Write.clicked.connect(self.write)

    def write(self):
        # 创建线程
        self.thread = WriteThread()
        # 连接信号
        self.thread._signal.connect(self.flush)
        # 开始线程
        self.thread.start()

    def flush(self, msg):
        print("flush " + msg)
        self.label_log.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
