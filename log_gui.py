import time
from PyQt5.Qt import *
from resource.action_log import Ui_Form
from ddbb import query_db
from gen_csv import save_file

HOUR_S = 3600
DAY_H = 24


class LogGui(QWidget, Ui_Form):
    current_le = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        str_time = time.strftime('%Y-%m-%d', time.localtime())
        self.st_le.setText(str_time)
        self.ed_le.setText(str_time)
        self.st_le.get_focus_signel.connect(lambda: self.set_cur_obj(self.st_le))
        self.ed_le.get_focus_signel.connect(lambda: self.set_cur_obj(self.ed_le))
        self.pd_le.get_focus_signel.connect(lambda: self.set_cur_obj())

    def fill_date(self):
        if not self.current_le:
            return
        date = self.calendarWidget.selectedDate()
        self.current_le.setText(date.toString('yyyy-MM-dd'))

    def set_cur_obj(self, cur_obj=None):
        self.current_le = cur_obj

    def gen_csv(self):
        start_time = self.st_le.text()
        end_time = self.ed_le.text()
        pd_no = self.pd_le.text()

        if start_time:
            start_time = time.mktime(time.strptime(start_time, '%Y-%m-%d'))
        if end_time:
            end_time = time.mktime(time.strptime(end_time, '%Y-%m-%d')) + HOUR_S * DAY_H
        if start_time > end_time:
            QMessageBox.information(self, 'Tips', 'wrong time information', QMessageBox.Ok)

        res, num = query_db(start_time, end_time, pd_no)
        # [print(r) for r in res]
        if not num:
            QMessageBox.information(self, '', 'Nobody operated during this period', QMessageBox.Ok)
            return
        res = save_file(res)
        if res:
            QMessageBox.information(self, '', 'generate successful', QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LogGui()
    window.show()
    sys.exit(app.exec_())
