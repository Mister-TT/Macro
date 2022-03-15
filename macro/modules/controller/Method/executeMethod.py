import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config
import time


class executeMethod(MethodInterface):
    def justDoit(self, controller):
        controller.hookHandler.compilerChangeHookState()
        time.sleep(0.1)
        executeFile = controller.returnExecuteFile()
        controller.compilerHandler.setState(config.EXECUTE, executeFile)
        controller.compilerHandler.start()


