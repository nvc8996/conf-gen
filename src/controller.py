import os
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QCheckBox, QFileDialog, QMessageBox
from src.loopWidget import LoopWidget
from src.inputWidget import InputWidget

from src.templateEngine import *

class Controller:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.temp_dir = TEMP_DIR
        self.out_dir = OUT_DIR
        self.data = {}

        self.load_templates()
        self.connect_ui()
        self.render()
    
    def connect_ui(self):
        # Add handlers for menu options
        self.ui.actionReset.triggered.connect(self.reset)
        self.ui.actionUnselect.triggered.connect(self.unselect_all)
        self.ui.actionSelect.triggered.connect(self.select_all)
        self.ui.actionAbout.triggered.connect(self.show_about)

        # Add handlers for buttons
        self.ui.genButton.clicked.connect(self.generate)
        self.ui.changeTempDirButton.clicked.connect(self.change_temp_dir)
        self.ui.changeOutDirButton.clicked.connect(self.change_out_dir)

    def load_templates(self):
        self.templates = []

        if not os.path.exists(self.temp_dir):
            return

        templates = os.listdir(self.temp_dir)

        for temp in templates:
            engine = TemplateEngine(self, temp, self.temp_dir)
            self.templates.append(engine)
    
    def update_vars(self):
        self.vars = []

        for temp in self.templates:
            if temp.enabled:
                for var in temp.vars:
                    if var not in self.vars:
                        self.vars.append(var)
    
    def render_templates(self):
        self.clear_templates()
        self.ui.verticalLayout.setAlignment(Qt.AlignTop)
        self.ui.verticalLayout.setContentsMargins(25, 0, 0, 0)

        for temp in self.templates:
            temp.checkBox = QCheckBox(temp.name)
            temp.checkBox.setChecked(True)
            temp.checkBox.stateChanged.connect(temp.set_enabled)
            temp.checkBox.setMinimumHeight(50)
            temp.checkBox.setMaximumHeight(50)
            self.ui.verticalLayout.addWidget(temp.checkBox)

    def render_inputs(self):
        self.clear_inputs()

        self.update_vars()

        self.data = {}

        target = self.ui.verticalLayout_2
        target.setAlignment(Qt.AlignTop)
        target.setSpacing(0)

        for var in self.vars:
            self.data[var.name] = InputWidget(var)
            target.addWidget(self.data[var.name])

        for temp in self.templates:
            if temp.enabled and temp.loop_count:
                for part in temp.loops:
                    widget = LoopWidget(part, temp.data)
                    target.addWidget(widget)

    def render(self):
        self.ui.tempDirLabel.setText(self.temp_dir)
        self.ui.tempDirLabel.setToolTip(self.temp_dir)
        self.ui.outDirLabel.setText(self.out_dir)
        self.ui.outDirLabel.setToolTip(self.out_dir)

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
    
    def unselect_all(self):
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().setChecked(False)
    
    def select_all(self):
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().setChecked(True)
        
    def show_about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle('Information')
        msg.setText('Config files generator by NVC version 1.0')

        msg.exec_()

    def generate(self):
        success = True
        try:
            for temp in self.templates:
                temp.generate()
            for temp in self.templates:
                temp.export(self.out_dir)
        except Exception as e:
            success = False
            error = str(e)

        msg = QMessageBox()

        if success:
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setWindowTitle('Information')
            msg.setText(f'Successfully generated files to {self.out_dir}')
        else:
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle('Warning')
            msg.setText(f'Failed.')
            msg.setDetailedText(error)

        msg.exec_()
    
    def change_temp_dir(self):
        res = str(QFileDialog.getExistingDirectory(self.ui.centralwidget, "Select templates folder"))
        if not res:
            return
        self.clear()
        self.temp_dir = res
        self.load_templates()
        self.render()

    def change_out_dir(self):
        res = str(QFileDialog.getExistingDirectory(self.ui.centralwidget, "Select output destination"))
        if not res:
            return
        self.out_dir = res
        self.ui.outDirLabel.setText(self.out_dir)
        self.ui.outDirLabel.setToolTip(self.out_dir)
    