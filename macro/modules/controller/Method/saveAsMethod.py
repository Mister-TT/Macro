import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.config import config
import os

class saveAsMethod(MethodInterface):
    def justDoit(self, controller):
        config.TMP_DIR = os.getcwd()
        config.TMP_DIR = eval(
            repr(config.TMP_DIR).replace('\\\\', '/'))
        self.Ui_DIR = os.path.abspath(os.path.dirname(__file__))
        self.Ui_DIR = eval(
            repr(self.Ui_DIR).replace('\\\\', '/'))


