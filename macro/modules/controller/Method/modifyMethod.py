import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config

class modifyMethod(MethodInterface):
    def justDoit(self, controller):
        controller.save(config.SAVE_DONT_TELL_ME)
        controller.compilerHandler.setState(config.MODIFY, config.TMP_FILE_PATH)
        controller.compilerHandler.start()


