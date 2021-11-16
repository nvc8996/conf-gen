import os
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QCheckBox, QFileDialog, QMessageBox
from src.loopWidget import LoopWidget
from src.inputWidget import InputWidget

from src.templateEngine import *

# Class for logic - controlling all features of the application
class Controller:
    def __init__(self, ui) -> None:
        self.ui = ui
        self.temp_dir = TEMP_DIR
        self.out_dir = OUT_DIR
        self.data = {}

        self.load_templates()
        self.connect_ui()
        self.render()
    
    # Connect GUI objects with their respective function
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

    # Load templates from folder
    def load_templates(self):
        # Init the list of templates
        self.templates = []

        # Quit if specified folder is not existing
        if not os.path.exists(self.temp_dir):
            return

        # Get list of template files in the folder
        templates = os.listdir(self.temp_dir)

        # Loop through all template files
        for temp in templates:
            # Create TemplateEngine object and add to templates list
            engine = TemplateEngine(self, temp, self.temp_dir)
            self.templates.append(engine)
    
    # Update the list of all basic variables (not included in any loop) from all selected templates
    def update_vars(self):
        # Init variables list
        self.vars = []

        # Loop through all template objects
        for temp in self.templates:
            # Consider only selected templates
            if temp.enabled:
                # All var from particular template
                for var in temp.vars:
                    # Consider only new variable - prevent duplicate
                    if var not in self.vars:
                        self.vars.append(var)
    
    # Render the list of templates with checkbox for user to select
    def render_templates(self):
        # Remove all existing widget
        self.clear_templates()

        # Set alignment and content margin
        self.ui.verticalLayout.setAlignment(Qt.AlignTop)
        self.ui.verticalLayout.setContentsMargins(25, 0, 0, 0)

        # Loop through all templates
        for temp in self.templates:
            # Create checkbox widget
            temp.checkBox = QCheckBox(temp.name)

            # Configure widget's sizes
            temp.checkBox.setMinimumHeight(50)
            temp.checkBox.setMaximumHeight(50)

            # Template is selected by default
            temp.checkBox.setChecked(True)

            # Connect state-changed event handler
            temp.checkBox.stateChanged.connect(temp.set_enabled)

            # Add widget to layout
            self.ui.verticalLayout.addWidget(temp.checkBox)

    # Render required inputs for user to fill, all fields must be filled in order to generate configuration files
    def render_inputs(self):
        # Clear all existing widgets
        self.clear_inputs()

        # Update variables list
        self.update_vars()

        # Reset data colection
        self.data = {}

        # Select target layout and configure alignment + spacing
        target = self.ui.verticalLayout_2
        target.setAlignment(Qt.AlignTop)
        target.setSpacing(0)

        # Loop through all basic variables
        for var in self.vars:
            # Create input widget and add to layout
            self.data[var.name] = InputWidget(var)
            target.addWidget(self.data[var.name])

        # Loop through all template to render widgets for loop's variables
        for temp in self.templates:
            # Consider only selected and having loop(s) template
            if temp.enabled and temp.loop_count:
                # Process each loop separately
                for part in temp.loops:
                    # Create input widget and add to layout
                    widget = LoopWidget(part, temp.data)
                    target.addWidget(widget)

    # Render GUI
    def render(self):
        # Set labels
        self.ui.tempDirLabel.setText(self.temp_dir)
        self.ui.tempDirLabel.setToolTip(self.temp_dir)
        self.ui.outDirLabel.setText(self.out_dir)
        self.ui.outDirLabel.setToolTip(self.out_dir)

        # Render other components
        self.render_templates()
        self.render_inputs()
    
    # Remove all existing template widgets
    def clear_templates(self):
        for i in reversed(range(self.ui.verticalLayout.count())):
            self.ui.verticalLayout.itemAt(i).widget().deleteLater()
        
    # Remove all existing input widgets
    def clear_inputs(self):
        for i in reversed(range(self.ui.verticalLayout_2.count())):
            self.ui.verticalLayout_2.itemAt(i).widget().deleteLater()
    
    # Clear all user's changes
    def clear(self):
        self.temp_dir = TEMP_DIR
        self.out_dir = OUT_DIR
        
        self.clear_inputs()
        self.clear_templates()
    
    # Reset the application
    def reset(self):
        self.clear()
        self.load_templates()
        self.render()
    
    # Unselect all template checkboxes
    def unselect_all(self):
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().setChecked(False)
    
    # Select all template checkboxes
    def select_all(self):
        for i in range(self.ui.verticalLayout.count()):
            self.ui.verticalLayout.itemAt(i).widget().setChecked(True)
        
    # Show information about the application
    def show_about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle('Information')
        msg.setText('Config files generator by NVC version 1.0')

        msg.exec_()

    # Generate configuration files based on user's inputs
    def generate(self):
        # Initially success state is true
        success = True

        try:
            # check if all templates are ready to generate
            for temp in self.templates:
                temp.generate()
            
            # Generate configuration files
            for temp in self.templates:
                temp.export(self.out_dir)
        except Exception as e:
            # Change success state and save error's message
            success = False
            error = str(e)

        # Display message to user based on success state
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
    
    # Change templates folder feature
    def change_temp_dir(self):
        # Get user's choice
        res = str(QFileDialog.getExistingDirectory(self.ui.centralwidget, "Select templates folder"))
        if not res:
            return
        
        # Update template
        self.temp_dir = res
        self.load_templates()
        self.render()

    # Change output destination folder
    def change_out_dir(self):
        # Get user's choice
        res = str(QFileDialog.getExistingDirectory(self.ui.centralwidget, "Select output destination"))
        if not res:
            return
        
        # Update output destination folder information
        self.out_dir = res
        self.ui.outDirLabel.setText(self.out_dir)
        self.ui.outDirLabel.setToolTip(self.out_dir)
    