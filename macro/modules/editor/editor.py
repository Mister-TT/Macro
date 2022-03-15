import os
import sys
from typing import ContextManager
sys.path.append("")

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QTextEdit, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

from macro.config import config

@config.Singleton
class Editor(QWebEngineView):
    def __init__(self, uiHandler, theme_type = 'white'):  # theme_type: black/white
        super().__init__()
        # 这下面是和主界面对接的时候，需要利用到的一些参数
        self.editor_flag = []
        self.uiHandler = uiHandler

        if theme_type == 'black':
            self.editor_index = (os.path.split(
                os.path.realpath(__file__))[0]) + "/index_black.html"
        else:
            self.editor_index = (os.path.split(
                os.path.realpath(__file__))[0]) + "/index_white.html"
        
        self.load(QUrl.fromLocalFile(self.editor_index))
        self.tmp_content = ""

    def set_monaco_html(self):
        # 这里是本地html路径,需根据实际情况进行修改.
        self.load(QUrl.fromLocalFile(self.editor_index))
    
    def set_theme_type(self, theme_type):
        if theme_type == 'black':
            self.editor_index = (os.path.split(
                os.path.realpath(__file__))[0]) + "/index_black.html"
        elif theme_type == 'white':
            self.editor_index = (os.path.split(
                os.path.realpath(__file__))[0]) + "/index_white.html"
        self.set_monaco_html()

    def save_content(self, content):   
        if(content == None):
            self.uiHandler.debugWindowHandler.append("文件内容为空")
            return

        try: 
            with open(config.TMP_FILE_PATH, 'w', encoding='UTF-8') as f:
                f.write(content)
                f.close()
        except FileNotFoundError:
            with open(config.TMP_FILE_PATH, 'w', encoding='UTF-8') as f:
                f.write(" ")
                f.close()
            with open(config.TMP_FILE_PATH, 'w', encoding='UTF-8') as f:
                f.write(content)
                f.close()

        if(self.need_call == config.SAVE_AND_TELL_ME):
            self.uiHandler.debugWindowHandler.append(
                "保存文件 " + config.TMP_FILE_PATH + " 成功")
            self.uiHandler.reload_editor()
        elif(self.need_call == config.SAVE_AND_CHECK):
            self.uiHandler.controllerHandler.check()
        elif(self.need_call == config.SAVE_AND_EXE):
            self.uiHandler.controllerHandler.execute(config.TMP_FILE_PATH)

    def toPlainText(self, call):
        """获取编辑器内容"""
        self.need_call = call
        self.page().runJavaScript(
            "monaco.editor.getModels()[0].getValue()", self.save_content)

    def setPlainText(self, data):
        """设置编辑器内容"""
        import base64
        data = base64.b64encode(data.encode())
        data = data.decode()
        # data = data.decode()
        self.page().runJavaScript(
            "monaco.editor.getModels()[0].setValue(Base64.decode('{}'))".format(data))


if __name__ == '__main__':
    app=QApplication(sys.argv)
    # win=Editor(1)   # 默认白色主题
    win = Editor(1, 'white')   # 黑色主题
    win.set_monaco_html()
    win.show()
    app.exit(app.exec_())

# 单个识别 √
# 语法检测 
