from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QWidget, QLabel, QVBoxLayout

from src.inputWidget import InputWidget

# Loop Widget class (handle user's input for loop)
class LoopWidget(QWidget):
    def __init__(self, loop_part, data) -> None:
        QWidget.__init__(self)
        self.loop_part = loop_part
        self.init_widget(data)
    
    def init_widget(self, data):
        # Init layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 0, 0, 0)
        self.layout.setSpacing(0)

        # Add label for name of the loop
        self.label = QLabel(self.loop_part.name)
        self.label.setStyleSheet('color: blue;')
        self.layout.addWidget(self.label)

        # Add ONE default sample part
        self.part_widget = PartWidget(self.loop_part, data)
        self.layout.addWidget(self.part_widget)

        # Add container for buttons
        buttons = QWidget()
        layout = QHBoxLayout(buttons)
        layout.setAlignment(Qt.AlignLeft)

        # Add button "Addition" - adding sample part
        addButton = QPushButton('+')
        addButton.setMaximumWidth(40)
        addButton.clicked.connect(self.part_widget.add_data_set)
        layout.addWidget(addButton)

        # Add button "Substitution" - remove last sample part
        addButton = QPushButton('-')
        addButton.setMaximumWidth(40)
        addButton.clicked.connect(self.part_widget.pop_data_set)
        layout.addWidget(addButton)

        # Add buttons container to layout
        self.layout.addWidget(buttons)

# Part Widget - handle user's input for loop sample. Might consist LoopWidget (for sub-loop).
class PartWidget(QWidget):
    def __init__(self, part, data) -> None:
        QWidget.__init__(self)
        self.part = part
        self.dataset = []
        data[part.name] = self.dataset
        self.init_widget()
        self.count = 0
        self.widgets = []

        # Initially loop has one sample
        self.add_data_set()
    
    # Init widget with vertical layout
    def init_widget(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 0, 0, 0)

    # Add inputs set for one sample
    def add_data_set(self):
        self.count += 1

        # Create container for ONE sample inputs
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setSpacing(0)

        # Add label for inputs set
        label = QLabel(f'Data set number {self.count}:')
        label.setStyleSheet('color: green;')
        layout.addWidget(label)

        # Add variable inputWidgets
        data = {}
        for var in self.part.vars:
            data[var.name] = InputWidget(var)
            layout.addWidget(data[var.name])
        
        # Add LoopWidget for loops
        for part in self.part.loops:
            loop_widget = LoopWidget(part, data)
            layout.addWidget(loop_widget)
        
        self.layout.addWidget(widget)
        self.widgets.append(widget)
        self.dataset.append(data)
    
    # Remove the last inputs set
    def pop_data_set(self):
        if len(self.dataset) > 1:
            self.widgets[-1].deleteLater()
            self.widgets.pop()
            self.dataset.pop()

            self.count -= 1