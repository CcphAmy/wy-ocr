# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from form import frmMain

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = frmMain.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
