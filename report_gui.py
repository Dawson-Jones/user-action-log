import time
import json
from PyQt5.Qt import *
from resource.report2 import Ui_Form
from gen_report.make_report import make_reports


class ReportGui(QWidget, Ui_Form):
    # send_signal = pyqtSignal(float, float, str, str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('生成报表工具')
        self.resize(500, 344)
        self.center()
        current_time = time.time()
        str_time = time.strftime('%Y-%m-%d', time.localtime(current_time - 3600 * 24))
        ed_time = time.strftime('%Y-%m-%d', time.localtime(current_time))
        self.st_time = str_time + ' 08:00:00'
        self.ed_time = ed_time + ' 08:00:00'
        self.st_le.setText(self.st_time)
        self.ed_le.setText(self.ed_time)
        self.le_regular()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def le_regular(self):
        reg_exp = QRegExp(
            '^\d{4}-(0?[1-9]|1[0-2])-(([012])?\d|3[01]) (([01])?\d|2[0-3]):[0-5]\d:[0-5]\d$'
        )
        time_limit = QRegExpValidator(reg_exp)
        self.st_le.setValidator(time_limit)
        self.ed_le.setValidator(time_limit)

    def gen_csv(self):
        st_time_str = self.st_le.text()
        ed_time_str = self.ed_le.text()

        st = 0
        ed = 0
        if st_time_str:
            try:
                st = time.mktime(time.strptime(st_time_str, '%Y-%m-%d %H:%M:%S'))
            except:
                self.tips('时间输入有误')
                self.st_le.setText(self.st_time)
                return
        if ed_time_str:
            try:
                ed = time.mktime(time.strptime(ed_time_str, '%Y-%m-%d %H:%M:%S'))
            except:
                self.tips('时间输入有误')
                self.ed_le.setText(self.ed_time)
                return
        if all([st, ed]) and st >= ed:
            self.tips('时间输入有误')
            return
        self.gen_btn.setEnabled(False)
        self.gen_btn.setText('GENERATING')
        thread = TSend(st, ed, st_time_str, ed_time_str)
        thread.signal.connect(self.tips)
        thread.start()
        thread.exec()
        # thread.wait()

    def tips(self, info: str):
        QMessageBox.information(self, '', info, QMessageBox.Ok)
        self.gen_btn.setEnabled(True)
        self.gen_btn.setText('GENERATE')


class TSend(QThread):
    signal = pyqtSignal(str)

    def __init__(self, st, ed, st_time_str, ed_time_str):
        super().__init__()
        self.st = st
        self.ed = ed
        self.st_time_str = st_time_str
        self.ed_time_str = ed_time_str

    def run(self):
        with open('config.json') as f:
            config = json.load(f)
        url = config.get('url')
        if not url:
            self.signal.emit('配置url出错')
        if make_reports(url, self.st, self.ed, self.st_time_str, self.ed_time_str):
            self.signal.emit('生成成功')
        else:
            self.signal.emit('生成失败')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ReportGui()
    window.show()
    sys.exit(app.exec_())
