import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QSystemTrayIcon, QAction, QMenu
from form.Tray import Tray
from config.LogConfig import LogConfig
from form.WScreenShot import WScreenShot
from form.FrmMain import Ui_MainWindow
from constant.AppConstant import App


def main():
    # 接受命令行参数
    app = QApplication(sys.argv)
    # 设置所有窗口不会被关闭
    QApplication.setQuitOnLastWindowClosed(False)
    # MainWindow
    mainWindow = QMainWindow()
    # 配置log
    LogConfig()
    # 加载截屏窗口
    screenShot = WScreenShot()
    # 加载主窗口
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    ui.btn_sreenShot.clicked.connect(screenShot.handleClick)
    ui.btn_ocr.clicked.connect(ui.ocr)
    # mainWindow.resize(App.MAIN_WINDOW_WIDTH, App.MAIN_WINDOW_HEIGHT)
    mainWindow.move(App.MAIN_WINDOW_LEFT, App.MAIN_WINDOW_TOP)
    mainWindow.setWindowTitle(App.MAIN_WINDOW_TITLE)

    # 加载托盘
    obj = Tray(mainWindow)
    obj.startTray()
    # 显示主窗口
    mainWindow.show()
    # 结束
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
