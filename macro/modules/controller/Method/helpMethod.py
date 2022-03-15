import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config
import webbrowser

class helpMethod(MethodInterface):
    def justDoit(self, controller):
        webbrowser.open(config.TMP_DIR + "/macro/modules/editor/help.html")


