import sys
from PyQt5.QtWidgets import *

from src.view import Ui_ConfGen
from src.controller import Controller

if __name__ == '__main__':
    app = QApplication([])
    
    MainWindow = QMainWindow()

    # load UI from view.py
    ui = Ui_ConfGen()
    # Setup UI on MainWindow
    ui.setupUi(MainWindow)

    # Set window title
    MainWindow.setWindowTitle("Configuration files generator")

    # Define controller
    controller = Controller(ui)
    
    # Show window
    MainWindow.show()

    # Run the app
    sys.exit(app.exec_())