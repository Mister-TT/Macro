# coding:utf-8
import sys
sys.path.append("")
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from macro.modules.UI.listener import listener
from PyQt5.QtGui import QCursor
from PyQt5 import QtWidgets, Qt
from PyQt5.QtCore import Qt
from macro.config import config

@config.Singleton
class watchWindow(QWidget, listener):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setWindowOpacity(0.80)  # 设置窗口透明度
        desktop = QApplication.desktop()
        X = 700
        Y = 50

        self.setStyleSheet("background-color: white;")
        self.setFixedSize(X, Y)  # 窗口大小
        self.move((desktop.width() - X) / 2, 0)
        # self.move(0,0)

        self.mainVLayout = QVBoxLayout(self)
        self.mainVLayout.setContentsMargins(0, 0, 0, 0)
        self.mainVLayout.setSpacing(0)

        # 公告标题
        self.notice_title = QLabel()
        self.notice_title.setMaximumWidth(700)
        self.notice_title.setMinimumWidth(700)
        self.notice_title.setAlignment(Qt.AlignCenter)
        self.notice_title.setStyleSheet(
            "font:63 11pt 微软雅黑;color:rgb(0,0,0); margin:10px 0px 5px;")

        # 将控件放入布局中
        self.mainVLayout.addWidget(self.notice_title)
        self.mainVLayout.addStretch(0)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos()-self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos()-self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def set_sub_window_text(self, content):
        self.notice_title.setText(content)  # 公告标题

    def announce(self, content):
        if(content[0] == "w"):
            self.notice_title.setText(content[1:-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = watchWindow()
    Main.show()
    sys.exit(app.exec_())
