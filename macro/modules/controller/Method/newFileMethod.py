import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config
import webbrowser

class newFileMethod(MethodInterface):
    def justDoit(self, controller):
        config.TMP_FILE_PATH = controller.fileManagerHandler.new_script_path("txt")
        config.TMP_FILE_PATH = eval(
            repr(config.TMP_FILE_PATH).replace('\\\\', '/'))


