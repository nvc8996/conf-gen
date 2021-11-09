from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget, QLabel, QVBoxLayout
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