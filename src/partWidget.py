from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout

from src.inputWidget import InputWidget

class PartWidget(QWidget):
    def __init__(self, part) -> None:
        QWidget.__init__(self)
        self.part = part
        self.init_widget()
        self.count = 0
        self.part.params = []
        self.labels = []
        self.add_data_set()
    
    def init_widget(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 0, 0, 0)

    def add_data_set(self):
        self.count += 1

        self.labels.append(QLabel(f'Data set number {self.count}:'))
        self.labels[-1].setStyleSheet('color: lightgreen;')
        self.layout.addWidget(self.labels[-1])

        data = {}
        for var in self.part.vars:
            data[var.name] = InputWidget(var)
            self.layout.addWidget(data[var.name])
        
        self.part.put_params(data)
    
    def pop_data_set(self):
        if len(self.part.params):
            data = self.part.params[-1]
            for widget in data.values():
                widget.deleteLater()
            
            self.part.pop_params()

            self.labels[-1].deleteLater()
            self.labels = self.labels[:-1]

            self.count -= 1