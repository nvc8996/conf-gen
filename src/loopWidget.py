from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QVBoxLayout
from src.partWidget import PartWidget

class LoopWidget(QWidget):
    def __init__(self, loop_part) -> None:
        QWidget.__init__(self)
        self.loop_part = loop_part
        self.init_widget()
    
    def init_widget(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 0, 0, 0)

        self.label = QLabel(self.loop_part.filename)
        self.label.setStyleSheet('color: lightblue;')
        self.layout.addWidget(self.label)

        self.part_widget = PartWidget(self.loop_part)
        self.layout.addWidget(self.part_widget)

        self.addButton = QPushButton('+')
        self.addButton.setMaximumWidth(40)
        self.addButton.clicked.connect(self.part_widget.add_data_set)
        self.layout.addWidget(self.addButton)

        self.addButton = QPushButton('-')
        self.addButton.setMaximumWidth(40)
        self.addButton.clicked.connect(self.part_widget.pop_data_set)
        self.layout.addWidget(self.addButton)