import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.modules.tech.ruler import ruler
from macro.config import config
from win32.lib import win32con

import time

class rulerMethod(MethodInterface):
    def justDoit(self, controller):
        controller.imageManagerHandler.showWindow(win32con.SW_MINIMIZE)
        time.sleep(0.25)
        controller.imageManagerHandler.window_capture("./cache/screenshot.jpg")
        controller.imageManagerHandler.low_image("./cache/screenshot.jpg", 1920, 1080, "./cache/screenshot.jpg")
        controller.imageManagerHandler.showWindow()
        controller.rulerHandler = ruler()
        controller.rulerHandler.showRuler()
        controller.imageManagerHandler.showWindow(win32con.SW_MAXIMIZE, "Figure 1", 1920, 1080)

