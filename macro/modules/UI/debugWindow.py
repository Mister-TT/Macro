from PyQt5 import QtWidgets
import sys
sys.path.append("")
from macro.config import config
from macro.modules.UI.listener import listener

@config.Singleton
class debugWindow(QtWidgets.QTextBrowser, listener):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setStyleSheet("")
        self.setObjectName(
            "textBrowser_editInformation")
        self.append("欢迎来到Macro！我是Debug窗口")

    def announce(self, content):
        if(content[0] == "d"):
            self.append(content[1:-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main = debugWindow()
    Main.show()
    sys.exit(app.exec_())

        

