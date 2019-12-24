from PyQt5.Qt import *
from resource.action_log import Ui_Form


class LogGui(QWidget, Ui_Form):
    current_le = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.st_le.get_focus_signel.connect(lambda: self.set_cur_obj(self.st_le))
        self.ed_le.get_focus_signel.connect(lambda: self.set_cur_obj(self.ed_le))

    def fill_date(self):
        if not self.current_le:
            return
        date = self.calendarWidget.selectedDate()
        self.current_le.setText(date.toString('yyyy-MM-dd'))
        self.current_le = None

    def set_cur_obj(self, cur_obj):
        self.current_le = cur_obj

    def gen_csv(self):
        print('generated')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LogGui()
    window.show()
    sys.exit(app.exec_())
