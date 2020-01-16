import threading
import sys
from log_gui import LogGui
from PyQt5.Qt import *
from gen_report.make_report import make_reports

window = None
flag = False


def make_report_res(st, et, st_str, et_str):
    global flag
    if make_reports(st, et, st_str, et_str):
        flag = True
    else:
        pass
        # window.gen_failed()


def lisen(button, gui):
    import time
    global flag
    while True:
        if flag:
            # gui.gen_success()
            button.setEnabled(True)
            QApplication.processEvents()
            flag = False
            gui.close()
        else:
            QApplication.processEvents()
            time.sleep(0.2)


def create_lisen(button, gui):
    thread = threading.Thread(target=lisen, args=(button, gui))
    thread.setDaemon(True)
    thread.start()


def create_thread(st, et, st_str, et_str):
    thread = threading.Thread(target=make_report_res, args=(st, et, st_str, et_str))
    thread.setDaemon(True)
    thread.start()


def main():
    app = QApplication(sys.argv)
    global window
    window = LogGui()
    create_lisen(window.gen_btn, window)
    window.show()
    # window.send_signal.connect(make_report_res)
    window.send_signal.connect(create_thread)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
