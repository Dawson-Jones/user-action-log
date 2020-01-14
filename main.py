import sys
from log_gui import LogGui
from PyQt5.Qt import *
from gen_report.make_report import make_report

window = None


def make_report_res(st, et, st_str, et_str):
    if make_report(st, et, st_str, et_str):
        window.gen_success()
        window.close()
    else:
        window.gen_failed()


def main():
    app = QApplication(sys.argv)
    global window
    window = LogGui()
    window.show()
    window.send_signal.connect(make_report_res)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
