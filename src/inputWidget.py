from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit

VALS = {
    "IP"    : QRegExpValidator(QRegExp("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")),
    "IPv4"  : QRegExpValidator(QRegExp("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")),
    "WORD"   : QRegExpValidator(QRegExp("\w*")),
    "NUM"   : QRegExpValidator(QRegExp("\d*")),
}

class InputWidget(QWidget):
    def __init__(self, var) -> None:
        QWidget.__init__(self)
        self.var = var
        self.value = ''
        self.init_widget()

    def init_widget(self):
        self.setMinimumHeight(45)
        self.setMaximumHeight(45)
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(0)

        self.label = QLabel(self.var.desc)
        self.label.setMinimumWidth(125)
        self.layout.addWidget(self.label)

        self.field = QLineEdit(self)
        if self.var.type in VALS.keys():
            self.field.setValidator(VALS[self.var.type])
        self.field.textEdited.connect(self.set_value)
        self.layout.addWidget(self.field)
    
    def set_value(self):
        self.value = self.field.text()