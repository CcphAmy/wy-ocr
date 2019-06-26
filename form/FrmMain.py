# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMain.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from util.OcrUtil import SouGoOcr


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 319)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 60, 531, 201))
        self.textEdit.setObjectName("textEdit")
        self.btn_sreenShot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sreenShot.setGeometry(QtCore.QRect(10, 10, 111, 41))
        self.btn_sreenShot.setObjectName("btn_sreenShot")
        self.btn_ocr = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ocr.setGeometry(QtCore.QRect(130, 10, 111, 41))
        self.btn_ocr.setObjectName("btn_ocr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_sreenShot.setText(_translate("MainWindow", "1 => 测试截图"))
        self.btn_ocr.setText(_translate("MainWindow", "2 => 文字识别"))

    def ocr(self):
        self.textEdit.setText(SouGoOcr.trans('screenShot.jpg'))
