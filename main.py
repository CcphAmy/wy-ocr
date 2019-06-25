from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QAction, QMenu, qApp, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

from form.frmMain import Ui_MainWindow  # Main Window
from config.LogConfig import LogConfig  # log
from constant.AppConstant import App  # Constant
import sys
import logging


class Main(object):
    """docstring for Main"""
    mainWindow = None
    ui = None
    tp = None
    tpMenu = None

    a1 = None
    a2 = None

    def __init__(self):
        super(Main, self).__init__()

    def quitApp(self):
        QCoreApplication.instance().quit()
        self.tp.setVisible(False)

    def startMain(self):
        self.mainWindow = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainWindow)

        # mainWindow.resize(App.MAIN_WINDOW_WIDTH, App.MAIN_WINDOW_HEIGHT)
        self.mainWindow.move(App.MAIN_WINDOW_LEFT, App.MAIN_WINDOW_TOP)
        self.mainWindow.setWindowTitle(App.MAIN_WINDOW_TITLE)
        self.mainWindow.show()

    def startTray(self):
        self.tp = QSystemTrayIcon(self.mainWindow)
        self.tp.setIcon(QIcon(App.ICON_PATH_NAME))  # todo 这个可能存在跨平台路径问题

        self.tpMenu = QMenu()

        self.a1 = QAction(text='Show', triggered=self.mainWindow.show)
        self.a2 = QAction(text='Exit', triggered=self.quitApp)

        self.tpMenu.addAction(self.a1)
        self.tpMenu.addAction(self.a2)
        self.tp.setContextMenu(self.tpMenu)
        self.tp.activated.connect(self.act)
        self.tp.show()

    def act(self, reason):
        logging.debug(reason)
        if reason == 2 or reason == 3:
            self.mainWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 接受命令行参数
    QApplication.setQuitOnLastWindowClosed(False)  # 设置所有窗口不会被关闭
    LogConfig()  # 配置log

    main = Main()
    main.startMain()
    main.startTray()
    sys.exit(app.exec_())
