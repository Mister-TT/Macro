from pythonwin import win32ui
from win32 import win32gui
from win32.lib import win32con
from win32 import win32api
import pyperclip
import sys
sys.path.append("")

import threading
import traceback
import time
import json
import copy
import pyWinhook
from time import sleep

from macro.modules.complier import CodeModifier
from macro.modules.complier import CodeJudger
from macro.modules.complier import CodeExcuter
from macro.modules.complier import Grammar
from PyQt5.QtCore import QThread, pyqtSignal
from macro.config import config
from os import path
from macro.logs import logger
from PIL import ImageGrab
from PIL import Image
import re

# 跑脚本的时候是用下面这个
class Complier(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(Complier, self).__init__()
        self.Grammar=Grammar.Grammar()
        self.Grammar.init()
        self.__modifier=CodeModifier.CodeModifier()
        self.__judger=CodeJudger.CodeJudger()
        self.__excuter=CodeExcuter.CodeExcuter()

        self.state = None
        self.filepath = None

    def getErrorList(self):
        return self.__judger.getErrorList()

    def modify(self,FilePath):
        self.__modifier.modifyFile(FilePath)

    def check(self,FilePath):
        if(self.__judger.judgeFile(FilePath)):
            print("编译通过")
            return True
        else:
            print("编译不通过")
            explist=self.__judger.getErrorList()
            for line in explist:
                print(line)
            return False

    def excute(self,FilePath):

        if(self.check(FilePath)):
            config.IS_RUNNING=1
            self.sinOut.emit("脚本开始运行")

            self.__excuter.excuteFile(FilePath, self)

            self.sinOut.emit("脚本执行结束")
            time.sleep(0.7)
            config.IS_RUNNING = 0

    def setState(self, state, filepath):
        self.state = state
        self.filepath = filepath

    def run(self):
        if(self.state == config.CHECK):
            if(self.check(self.filepath)):
                self.sinOut.emit(config.CHECK_GOOD_MES)
            else:
                self.sinOut.emit(config.CHECK_BAD_MES)
        
        elif(self.state == config.MODIFY):
            self.modify(self.filepath)
            self.sinOut.emit(config.MODIFY_GOOD_MES)
        
        elif(self.state == config.EXECUTE):
            self.excute(self.filepath)


if __name__=='__main__':
    file_path="C:\\Users\\74068\\Desktop\\实训\\uml\\macro\\modules\\complier\\test.txt" 
    t=Complier(threading.Event())
    t.modify(file_path)
    t.excute(file_path)
    #print(re.search(r"变量 (.*?)","整型 变量 2323232232"))
