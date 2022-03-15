import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.modules.tech.hook import waitingState, workingState
from macro.config import config
from win32.lib import win32con

class monitorMethod(MethodInterface):
    def justDoit(self, controller):
        if(isinstance(controller.Hook_get_state(), waitingState)):
            controller.imageManagerHandler.showWindow(win32con.SW_MINIMIZE)
            controller.countWindowHandler.initAndShow()
            controller.countWindowHandler.show()
            controller.countWindowThreading.start()
            controller.hookHandler.change_state()
        elif(isinstance(controller.Hook_get_state(), workingState)):
            callback = controller.hookHandlerChangeState()
            controller.fileManagerHandler.hookWriteEvent(callback[0], config.TMP_FILE_PATH, callback[1])
            controller.open(filepath = config.TMP_FILE_PATH, call=False)
            controller.imageManagerHandler.showWindow(win32con.SW_SHOWNORMAL)

