import os

from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QLabel, QLineEdit, QWidget

from src.templateEngine import *

class Controller:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.temp_dir = TEMP_DIR
        self.out_dir = OUT_DIR
        self.load_templates()
        self.render()
        self.ui.actionReset.triggered.connect(self.reset)
    
    def load_templates(self):
        self.templates = []
        templates = os.listdir(self.temp_dir)

        for temp in templates:
            engine = TemplateEngine(self, temp)
            self.templates.append(engine)
    
    def update_vars(self):
        self.vars = set()

        for temp in self.templates:
            if temp.enabled:
                self.vars |= temp.vars
    
    def render_templates(self):
        self.clear_templates()

        for temp in self.templates:
            temp.checkBox = QCheckBox(temp.name)
            temp.checkBox.setChecked(True)
            temp.checkBox.stateChanged.connect(temp.set_enabled)
            self.ui.verticalLayout.addWidget(temp.checkBox)
    
    def create_input(self, var):
        widget = QWidget()
        widget.setMinimumHeight(30)
        layout = QHBoxLayout(widget)

        label = QLabel(var.desc)
        label.setMinimumWidth(150)
        field = QLineEdit()
        layout.addWidget(label)
        layout.addWidget(field)

        return widget

    def render_inputs(self):
        self.clear_inputs()

        self.update_vars()

        target = self.ui.verticalLayout_2
        for var in self.vars:
            widget = self.create_input(var)
            target.addWidget(widget)

    def render(self):
        self.ui.tempDirLabel.setText(self.temp_dir)
        self.ui.outDirLabel.setText(self.out_dir)
        self.render_templates()
        self.render_inputs()
    
    def clear_templates(self):
        for i in reversed(range(self.ui.verticalLayout.count())):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        
    def clear_inputs(self):
        for i in reversed(range(self.ui.verticalLayout_2.count())):
            self.ui.verticalLayout_2.itemAt(i).widget().deleteLater()
    
    def clear(self):
        self.temp_dir = TEMP_DIR
        self.out_dir = OUT_DIR
        
        self.clear_inputs()
        self.clear_templates()
    
    def reset(self):
        self.clear()
        self.load_templates()
        self.render()
        