# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confGen.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 111, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.listConfFiles = QtWidgets.QScrollArea(self.centralwidget)
        self.listConfFiles.setGeometry(QtCore.QRect(12, 42, 211, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listConfFiles.sizePolicy().hasHeightForWidth())
        self.listConfFiles.setSizePolicy(sizePolicy)
        self.listConfFiles.setWidgetResizable(True)
        self.listConfFiles.setObjectName("listConfFiles")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 509))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listConfFiles.setWidget(self.scrollAreaWidgetContents)
        self.listInputs = QtWidgets.QScrollArea(self.centralwidget)
        self.listInputs.setGeometry(QtCore.QRect(240, 40, 511, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listInputs.sizePolicy().hasHeightForWidth())
        self.listInputs.setSizePolicy(sizePolicy)
        self.listInputs.setWidgetResizable(True)
        self.listInputs.setObjectName("listInputs")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 509, 509))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listInputs.setWidget(self.scrollAreaWidgetContents_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(405, 12, 127, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.tempDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.tempDirLabel.setGeometry(QtCore.QRect(790, 80, 68, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tempDirLabel.sizePolicy().hasHeightForWidth())
        self.tempDirLabel.setSizePolicy(sizePolicy)
        self.tempDirLabel.setObjectName("tempDirLabel")
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(780, 510, 98, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genButton.sizePolicy().hasHeightForWidth())
        self.genButton.setSizePolicy(sizePolicy)
        self.genButton.setObjectName("genButton")
        self.changeTempDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeTempDirButton.setGeometry(QtCore.QRect(770, 100, 113, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeTempDirButton.sizePolicy().hasHeightForWidth())
        self.changeTempDirButton.setSizePolicy(sizePolicy)
        self.changeTempDirButton.setObjectName("changeTempDirButton")
        self.changeOutDirButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeOutDirButton.setGeometry(QtCore.QRect(770, 190, 113, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changeOutDirButton.sizePolicy().hasHeightForWidth())
        self.changeOutDirButton.setSizePolicy(sizePolicy)
        self.changeOutDirButton.setObjectName("changeOutDirButton")
        self.outDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.outDirLabel.setGeometry(QtCore.QRect(790, 170, 60, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outDirLabel.sizePolicy().hasHeightForWidth())
        self.outDirLabel.setSizePolicy(sizePolicy)
        self.outDirLabel.setObjectName("outDirLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 24))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUnselect = QtWidgets.QAction(MainWindow)
        self.actionUnselect.setObjectName("actionUnselect")
        self.actionSelect = QtWidgets.QAction(MainWindow)
        self.actionSelect.setObjectName("actionSelect")
        self.menuMenu.addAction(self.actionReset)
        self.menuMenu.addAction(self.actionSelect)
        self.menuMenu.addAction(self.actionUnselect)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Configuration files"))
        self.label_2.setText(_translate("MainWindow", "Required parameters"))
        self.tempDirLabel.setText(_translate("MainWindow", "./templates"))
        self.genButton.setText(_translate("MainWindow", "Generate"))
        self.changeTempDirButton.setText(_translate("MainWindow", "Change"))
        self.changeOutDirButton.setText(_translate("MainWindow", "Change"))
        self.outDirLabel.setText(_translate("MainWindow", "./configs"))
        self.menuMenu.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUnselect.setText(_translate("MainWindow", "Unselect all"))
        self.actionSelect.setText(_translate("MainWindow", "Select all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
