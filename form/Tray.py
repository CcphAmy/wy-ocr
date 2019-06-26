# -*- coding: utf-8 -*- 
# @Time : 2019/6/26 下午12:28 
# @Author : CcphAmy 
# @Site :  
# @File : Tray.py.py

from PyQt5.QtWidgets import QMainWindow, QSystemTrayIcon, QAction, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

from constant.AppConstant import App
import logging


class Tray(object):
    """docstring for Main"""
    mainWindow = None
    tray = None
    trayMenu = None
    menuOptionShow = None
    menuOptionExit = None

    def __init__(self, mainWindow):
        super(Tray, self).__init__()
        self.mainWindow = mainWindow

    def quitApp(self):
        QCoreApplication.instance().quit()
        self.tray.setVisible(False)

    def startTray(self):
        self.tray = QSystemTrayIcon(self.mainWindow)
        self.tray.setIcon(QIcon(App.ICON_PATH_NAME))

        self.trayMenu = QMenu()

        self.menuOptionShow = QAction(text='Show', triggered=self.mainWindow.show)
        self.menuOptionExit = QAction(text='Exit', triggered=self.quitApp)

        self.trayMenu.addAction(self.menuOptionShow)
        self.trayMenu.addAction(self.menuOptionExit)
        self.tray.setContextMenu(self.trayMenu)
        self.tray.activated.connect(self.act)
        self.tray.show()

    def act(self, reason):
        logging.debug(reason)
        if reason == 2 or reason == 3:
            self.mainWindow.show()
