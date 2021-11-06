import os
import sys
from PyQt5.QtWidgets import *

from src.templateEngine import *
from src.view import Ui_MainWindow

templates = os.listdir(TEMP_DIR)

if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.outDirLabel.setText(OUT_DIR)
    ui.tempDirLabel.setText(TEMP_DIR)

    # layout = QVBoxLayout()
    # ui.listConfFiles.setLayout(layout)
    for temp in templates:
        tmp = QCheckBox(temp[:-4])
        tmp.setChecked(True)
        # layout.addWidget(tmp)
        ui.verticalLayout.addWidget(tmp)
    
    MainWindow.show()

    sys.exit(app.exec_())