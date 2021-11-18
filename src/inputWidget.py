from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QPushButton, QWidget, QHBoxLayout, QLabel, QLineEdit, QVBoxLayout

# Type's value validators
VALS = {
    "IP"    : QRegExpValidator(QRegExp("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")),
    "IPv4"  : QRegExpValidator(QRegExp("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")),
    "WORD"   : QRegExpValidator(QRegExp("\w*")),
    "NUM"   : QRegExpValidator(QRegExp("\d*")),
}

# In the future type can be used to customize input field, in example: checkbox, combobox, ...

# Custom input widget for one variable
class InputWidget(QWidget):
    def __init__(self, var) -> None:
        QWidget.__init__(self)
        self.var = var
        self.value = ''

        # Customize widget
        self.init_widget()

    # Init widget with custom content
    def init_widget(self):
        # Create horizontal layout
        self.layout = QHBoxLayout(self)

        # Add variable description to layout
        self.label = QLabel(self.var.desc)
        self.label.setMinimumWidth(125)
        self.layout.addWidget(self.label)

        # Add input field to layout
        if self.var.type.startswith('LIST_'):
            self.field = ListWidget(self.var.type, self)
        else:
            self.field = QLineEdit(self)
            if self.var.type in VALS.keys():
                self.field.setValidator(VALS[self.var.type])
            self.field.textEdited.connect(self.set_value)
        self.layout.addWidget(self.field)
    
    # Set value handler
    def set_value(self):
        self.value = self.field.text()

# Input Widget for list variable
class ListWidget(QWidget):
    def __init__(self, type, master) -> None:
        QWidget.__init__(self)
        self.type = type[5:]
        self.master = master
        self.cnt = 0
        self.inputs = []
        self.input_lines = []

        # Customize widget
        self.init_widget()

    # Init widget with custom content
    def init_widget(self):
        # Create horizontal layout
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)

        # Create container widget for list of inputs
        self.container = QWidget()
        self.c_layout = QVBoxLayout(self.container)

        # Add container widget to main widget
        self.layout.addWidget(self.container)

        # Add container for buttons
        buttons = QWidget()
        layout = QHBoxLayout(buttons)
        layout.setAlignment(Qt.AlignLeft)

        # Add button "Addition" - adding input
        addButton = QPushButton('+')
        addButton.setMaximumWidth(30)
        addButton.setMinimumWidth(30)
        addButton.clicked.connect(self.add_input)
        layout.addWidget(addButton)

        # Add button "Substitution" - remove last input
        removeButton = QPushButton('-')
        removeButton.setMaximumWidth(30)
        removeButton.setMinimumWidth(30)
        removeButton.clicked.connect(self.remove_input)
        layout.addWidget(removeButton)

        # Add buttons to main widget
        self.layout.addWidget(buttons)
        
        self.add_input()

    
    # Add new input to inputs list (increase the number of values)
    def add_input(self):
        # Increase counter
        self.cnt += 1

        # Widget for input
        line = QWidget()
        layout = QHBoxLayout(line)

        # Label - index of input
        label = QLabel(str(self.cnt))
        label.setMaximumWidth(20)
        layout.addWidget(label)

        # Input itself
        input = QLineEdit(self)
        if self.type in VALS.keys():
            input.setValidator(VALS[self.type])
        input.textEdited.connect(self.set_value)
        layout.addWidget(input)

        #  Add line widget to container widget
        self.c_layout.addWidget(line)

        # Save line and input widget for management
        self.input_lines.append(line)
        self.inputs.append(input)

    # Delete input from inputs list (decrease the number of values)
    def remove_input(self):
        # Do not remove if there's only one input
        if self.cnt < 2:
            return
        
        # Remove widget
        self.input_lines[-1].deleteLater()
        
        # Update management lists
        self.inputs.pop()
        self.input_lines.pop()

        # Update counter
        self.cnt -= 1

        # Update variable value
        self.set_value()


    # Set value handler
    def set_value(self):
        self.master.set_value()

    # Formulate value from inputs
    def text(self):
        text = ','.join([input.text() for input in self.inputs])
        return text
