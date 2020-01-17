import time
from PyQt5.Qt import *
from resource.action_log import Ui_Form

HOUR_S = 3600
DAY_H = 24


class LogGui(QWidget, Ui_Form):
    current_le = None
    send_signal = pyqtSignal(float, float, str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        str_time = time.strftime('%Y-%m-%d', time.localtime())
        self.st_le.setText(str_time)
        self.ed_le.setText(str_time)
        self.st_le.get_focus_signel.connect(lambda: self.set_cur_obj(self.st_le))
        self.ed_le.get_focus_signel.connect(lambda: self.set_cur_obj(self.ed_le))

    def fill_date(self):
        if not self.current_le:
            return
        date = self.calendarWidget.selectedDate()
        self.current_le.setText(date.toString('yyyy-MM-dd'))

    def set_cur_obj(self, cur_obj=None):
        self.current_le = cur_obj

    def gen_csv(self):
        self.gen_btn.setStyleSheet('background-color: rgb(127,127,127)')
        self.gen_btn.setEnabled(False)
        start_time_str = self.st_le.text()
        end_time_str = self.ed_le.text()

        if start_time_str:
            try:
                start_time = time.mktime(time.strptime(start_time_str, '%Y-%m-%d'))
            except Exception:
                self.gen_failed()
        if end_time_str:
            try:
                end_time = time.mktime(time.strptime(end_time_str, '%Y-%m-%d')) + HOUR_S * DAY_H
            except Exception:
                self.gen_failed()
        if all([start_time_str, end_time_str]) and start_time >= end_time:
            QMessageBox.information(self, 'Tips', 'wrong time information', QMessageBox.Ok)
            return

        # res, num = query_db(start_time, end_time, pd_no)
        self.send_signal.emit(start_time, end_time, start_time_str, end_time_str)

    def gen_success(self):
        QMessageBox.information(self, '', 'generate successful', QMessageBox.Ok)

    def gen_failed(self):
        QMessageBox.information(self, '', '失败', QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LogGui()
    window.show()
    sys.exit(app.exec_())
