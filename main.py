import sys
from PyQt5.QtWidgets import *

from src.view import Ui_ConfGen
from src.controller import Controller

if __name__ == '__main__':
    app = QApplication([])
    
    MainWindow = QMainWindow()

    ui = Ui_ConfGen()
    ui.setupUi(MainWindow)

    controller = Controller(ui)
    
    MainWindow.show()

    sys.exit(app.exec_())