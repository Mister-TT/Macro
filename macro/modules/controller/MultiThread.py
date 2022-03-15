from macro.modules.tech.voiceManager import voiceManager
from macro.modules.UI.countWindow import countWindow
from PyQt5.QtCore import QThread, pyqtSignal
import time

import sys
sys.path.append("")

from macro.config import config

class myVoiceThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, threadID, name, fileHandler):
        super().__init__()
        self.voiceManagerHandler = voiceManager()
        self.voiceManagerHandler.setVoiceThreading(self)
        self.fileHandler = fileHandler
        self.threadID = threadID
        self.name = name

    def getVoiceManager(self):
        return self.voiceManagerHandler

    def saveTextFile(self, content):
        self.fileHandler.mkdir("scripts")
        
        new = open(config.TMP_FILE_PATH, "a", encoding='utf-8')
        new.write("\n\n")
        new.write(content[0])
        new.close()

    def run(self):
        self.voiceManagerHandler.myVoiceRecord()

        if(self.voiceManagerHandler.getState() == config.VOICE_RECORD_RECORDING):
            self.voiceManagerHandler.changeVoiceManagerState()

        self.sinOut.emit("开始进行语音识别")
        content = self.voiceManagerHandler.myVoiceRecognize()
        if(content == "--"):
            self.sinOut.emit("语音识别失败！")
        else:
            self.sinOut.emit("语音识别成功！")
            self.saveTextFile(content)

        self.sinOut.emit("ok")

class myCountWindowThread(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self, threadID, name):
        super().__init__()
        self.countWindowHandler = countWindow()
        self.threadID = threadID
        self.name = name

    def getCountWindow(self):
        return self.countWindowHandler

    def run(self):
        cishu = 0
        while (cishu < 3):  # 秒
            time.sleep(1)
            cishu += 1
            self.sinOut.emit("click")
            
        self.sinOut.emit("ok")