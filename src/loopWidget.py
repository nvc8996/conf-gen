from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget, QLabel, QVBoxLayout

from src.inputWidget import InputWidget


class LoopWidget(QWidget):
    def __init__(self, loop_part, data) -> None:
        QWidget.__init__(self)
        self.loop_part = loop_part
        self.init_widget(data)
    
    def init_widget(self, data):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 0, 0, 0)
        self.layout.setSpacing(0)

        self.label = QLabel(self.loop_part.name)
        self.label.setStyleSheet('color: lightblue;')
        self.layout.addWidget(self.label)

        self.part_widget = PartWidget(self.loop_part, data)
        self.layout.addWidget(self.part_widget)

        buttons = QWidget()
        layout = QHBoxLayout(buttons)
        layout.setAlignment(Qt.AlignLeft)

        addButton = QPushButton('+')
        addButton.setMaximumWidth(40)
        addButton.clicked.connect(self.part_widget.add_data_set)
        layout.addWidget(addButton)

        addButton = QPushButton('-')
        addButton.setMaximumWidth(40)
        addButton.clicked.connect(self.part_widget.pop_data_set)
        layout.addWidget(addButton)

        self.layout.addWidget(buttons)

class PartWidget(QWidget):
    def __init__(self, part, data) -> None:
        QWidget.__init__(self)
        self.part = part
        self.dataset = []
        data[part.name] = self.dataset
        self.init_widget()
        self.count = 0
        self.widgets = []

        self.add_data_set()
    
    def init_widget(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 0, 0, 0)

    def add_data_set(self):
        self.count += 1

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)

        label = QLabel(f'Data set number {self.count}:')
        label.setStyleSheet('color: lightgreen;')
        layout.addWidget(label)

        data = {}
        for var in self.part.vars:
            data[var.name] = InputWidget(var)
            layout.addWidget(data[var.name])
        
        for part in self.part.loops:
            loop_widget = LoopWidget(part, data)
            layout.addWidget(loop_widget)
        
        self.layout.addWidget(widget)
        self.widgets.append(widget)
        self.dataset.append(data)
    
    def pop_data_set(self):
        if len(self.dataset) > 1:
            self.widgets[-1].deleteLater()
            self.widgets.pop()
            self.dataset.pop()

            self.count -= 1