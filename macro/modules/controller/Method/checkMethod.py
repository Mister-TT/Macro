import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config

class checkMethod(MethodInterface):
    def justDoit(self, controller):
        controller.compilerHandler.setState(config.CHECK, config.TMP_FILE_PATH)
        controller.compilerHandler.start()


