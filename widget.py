from PyQt5.Qt import *


class ReWriteLe(QLineEdit):
    get_focus_signel = pyqtSignal()

    def __init__(self, *args):
        super().__init__(*args)

    def focusInEvent(self, QFocusEvent):
        self.get_focus_signel.emit()
