from PyQt5.QtWidgets import QDesktopWidget, QApplication, QWidget
from PyQt5.QtGui import QBitmap, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint, QRect

import sys


class WScreenShot(QWidget):
    storePath = 'screenShot.jpg'
    imageType = 'JPG'
    quality = 100

    def __init__(self, parent=None):
        super(WScreenShot, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet('''background-color:black; ''')
        self.setWindowOpacity(0.6)
        desktopRect = QDesktopWidget().screenGeometry()
        self.setGeometry(desktopRect)
        self.setCursor(Qt.CrossCursor)
        self.blackMask = QBitmap(desktopRect.size())
        self.blackMask.fill(Qt.black)
        self.mask = self.blackMask.copy()
        self.isDrawing = False
        self.startPoint = QPoint()
        self.endPoint = QPoint()

    def paintEvent(self, event):
        if self.isDrawing:
            self.mask = self.blackMask.copy()
            pp = QPainter(self.mask)
            pen = QPen()
            pen.setStyle(Qt.NoPen)
            pp.setPen(pen)
            brush = QBrush(Qt.white)
            pp.setBrush(brush)
            pp.drawRect(QRect(self.startPoint, self.endPoint))
            self.setMask(QBitmap(self.mask))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.endPoint = self.startPoint
            self.isDrawing = True

    def mouseMoveEvent(self, event):
        if self.isDrawing:
            self.endPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            screenShot = QApplication.primaryScreen().grabWindow(QApplication.desktop().winId())
            rect = QRect(self.startPoint, self.endPoint)
            outputRegion = screenShot.copy(rect)
            outputRegion.save(self.storePath, format=self.imageType, quality=self.quality)
            self.close()

    def handleClick(self):
        if not self.isVisible():
            self.show()

    def handleClose(self):
        self.close()