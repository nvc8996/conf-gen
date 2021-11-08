from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit

class InputWidget(QWidget):
    def __init__(self, var) -> None:
        QWidget.__init__(self)
        self.var = var
        self.value = ''
        self.init_widget()

    def init_widget(self):
        self.setMinimumHeight(50)
        self.setMaximumHeight(50)
        self.layout = QHBoxLayout(self)

        self.label = QLabel(self.var.desc)
        self.label.setMinimumWidth(175)
        self.layout.addWidget(self.label)

        self.field = QLineEdit(self)
        self.field.textEdited.connect(self.set_value)
        self.layout.addWidget(self.field)
    
    def set_value(self):
        self.value = self.field.text()