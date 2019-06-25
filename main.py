from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QAction, QMenu, qApp, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

# CONSTANT
from constant.AppConstant import App
import sys
import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG) # 只执行一次配置即可，后面将logging的配置封装一下

    app = QApplication(sys.argv)
    QApplication.setQuitOnLastWindowClosed(False)  # 设置所有窗口不会被关闭
    mainWindow = QWidget()
    # mainWindow.resize(250, 250)
    mainWindow.move(300, 300)
    mainWindow.setWindowTitle(App.MAIN_WINDOW_TITLE)
    mainWindow.show()

    tp = QSystemTrayIcon(mainWindow)
    tp.setIcon(QIcon(App.ICON_PATH_NAME))  # todo 这个可能存在跨平台路径问题

    a1 = QAction('&显示(Show)', triggered = mainWindow.show)


    def quitApp():
        mainWindow.show()
        re = QMessageBox.question(mainWindow, "提示", "退出系统", QMessageBox.Yes |
                                  QMessageBox.No, QMessageBox.No)
        if re == QMessageBox.Yes:
            QCoreApplication.instance().quit()
            tp.setVisible(False)


    a2 = QAction('&退出(Exit)', triggered = quitApp)

    tpMenu = QMenu()
    tpMenu.addAction(a1)
    tpMenu.addAction(a2)
    tp.setContextMenu(tpMenu)
    tp.show()

    # 信息提示
    # 参数1：标题
    # 参数2：内容
    # 参数3：图标（0没有图标 1信息图标 2警告图标 3错误图标），0还是有一个小图标
    tp.showMessage('test', 'tray', icon=0)


    def message():
        print("弹出的信息被点击了")


    tp.messageClicked.connect(message)


    def act(reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        logging.debug(reason)
        if reason == 2 or reason == 3:
            mainWindow.show()


    tp.activated.connect(act)
    sys.exit(app.exec_())
