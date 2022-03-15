import sys
sys.path.append("")


from macro.modules.controller.Method.helpMethod import helpMethod
from macro.modules.controller.Method.voiceMethod import voiceMethod
from macro.modules.controller.Method.monitorMethod import monitorMethod
from macro.modules.controller.Method.checkMethod import checkMethod
from macro.modules.controller.Method.modifyMethod import modifyMethod
from macro.modules.controller.Method.executeMethod import executeMethod
from macro.modules.controller.Method.rulerMethod import rulerMethod
from macro.modules.controller.Method.saveAsMethod import saveAsMethod
from macro.modules.controller.Method.newFileMethod import newFileMethod
from macro.modules.controller.Method.openMethod import openMethod
from macro.modules.controller.Method.closeAndSaveMethod import closeAndSaveMethod

from win32.lib import win32con

from macro.modules.controller.MultiThread import myVoiceThread, myCountWindowThread
from macro.modules.tech.imageManager import imageManager
from macro.modules.tech.fileManager import fileManager
from macro.modules.complier.complier import Complier
from macro.modules.UI.countWindow import countWindow
from macro.modules.tech.hook import hook
from macro.config import config
from macro.logs import logger



class controller():
    def __init__(self, watchWindowHandler, debugWindowHandler, editorHandler):
        self.hookHandler = hook(self.monitor)
        self.imageManagerHandler = imageManager()
        self.fileManagerHandler = fileManager()
        self.debugWindowHandler = debugWindowHandler
        self.watchWindowHandler = watchWindowHandler
        self.editorHandler = editorHandler
        
        # 设置声音的对象
        self.voiceThreading = myVoiceThread(10086, "voiceThreading", self.fileManagerHandler)
        self.voiceThreading.sinOut.connect(self.getVoiceThreadMessage)
        self.voiceManagerHandler = self.voiceThreading.getVoiceManager()

        # 倒数窗口
        self.countWindowThreading = myCountWindowThread(10087, "countWindowThread")
        self.countWindowThreading.sinOut.connect(self.getCountWindowThreadMessage)
        self.countWindowHandler = self.countWindowThreading.getCountWindow()
 
        # 编译器的返回消息
        self.compilerHandler = Complier()
        self.compilerHandler.sinOut.connect(self.getCompilerMessage)

        # 创建一些基础的信息
        self.fileManagerHandler.mkdir("cache")
        self.fileManagerHandler.mkdir("img")
        self.fileManagerHandler.mkdir("scripts")
        self.openFile = None
        self.executeFile = None
        self.callOfSave = None

        # 一些策略
        self.helpMethod = helpMethod()
        self.voiceMethod = voiceMethod()
        self.monitorMethod = monitorMethod()
        self.checkMethod = checkMethod()
        self.modifyMethod = modifyMethod()
        self.executeMethod = executeMethod()
        self.rulerMethod = rulerMethod()
        self.saveAsMethod = saveAsMethod()
        self.newFileMethod = newFileMethod()
        self.openMethod = openMethod()
        self.closeAndSaveMethod = closeAndSaveMethod()

    # 未使用策略模式的实现
    def addPushButtonSubscriber_Hook(self, subScriber):
        self.hookHandler.addPushButtonSubscriber(subScriber)

    def addWindowSubscriber_Hook(self, subScriver):
        self.hookHandler.addWindowSubscriber(subScriver)

    def search(self, keyWord):
        return self.fileManagerHandler.search(keyWord)

    def Minimize(self):
        self.imageManagerHandler.showWindow(win32con.SW_MINIMIZE)

    def cleardebugWindow(self):
        self.debugWindowHandler.clear()

    def save(self, call):
        self.editorHandler.toPlainText(call)

    def remove(self, filepath):
        self.fileManagerHandler.remove(filepath)

    def image(self):
        self.fileManagerHandler.controllerImageFile()

    # 使用了策略模式的实现
    def help(self):
        self.helpMethod.justDoit(self)

    def voice(self):
        self.voiceMethod.justDoit(self)

    def monitor(self):
        self.monitorMethod.justDoit(self)

    def check(self):
        self.checkMethod.justDoit(self)

    def modify(self):
        self.modifyMethod.justDoit(self)

    def execute(self, filepath):
        self.executeFile = filepath
        self.executeMethod.justDoit(self)
    
    def showRuler(self):
        self.rulerMethod.justDoit(self)

    def saveAs(self):
        self.saveAsMethod.justDoit(self)

    def newFile(self):
        self.newFileMethod.justDoit(self)

    def closeAndSave(self):
        self.closeAndSaveMethod.justDoit(self)

    def open(self, filepath = "", call = True):
        self.openFile = filepath
        self.callOfSave = call
        self.openMethod.justDoit(self)

    def newPage(self):
        pass

    # 返回值
    def returnOpenFile(self):
        return self.openFile
    
    def returnCallOfSave(self):
        return self.callOfSave

    def returnExecuteFile(self):
        return self.executeFile

    def hookHandlerChangeState(self):
        return self.hookHandler.change_state()

    def Hook_get_state(self):
        return self.hookHandler.get_state()


    # 回调函数
    def getVoiceThreadMessage(self, result):
        if(result == "ok"):
            self.open(config.TMP_FILE_PATH, call = False)
        else:
            self.debugWindowHandler.append(result)

    def getCountWindowThreadMessage(self, result):
        if(result == "click"):
            self.countWindowHandler.Click()        
        elif(result == "ok"):
            print("倒计时窗口正常结束")
            self.save(config.SAVE_DONT_TELL_ME)
            self.hookHandlerChangeState()

    def getCompilerMessage(self, content):
        if content == config.CHECK_GOOD_MES:
            self.watchWindowHandler.set_sub_window_text("通过检查！")

        elif content == config.CHECK_BAD_MES:
            self.watchWindowHandler.set_sub_window_text("未通过检查！")
            for line in self.compilerHandler.getErrorList():
                self.debugWindowHandler.append(line)

        elif content == config.MODIFY_GOOD_MES:
            self.open(config.TMP_FILE_PATH, False)
            self.save(config.SAVE_DONT_TELL_ME)

        else:
            print(content)
            self.watchWindowHandler.set_sub_window_text(content)

if __name__ == "__main__":
    pass