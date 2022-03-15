from win32 import win32api
from win32.lib import win32con
from win32 import win32gui
from pythonwin import win32ui
import threading
from time import sleep
import sys
sys.path.append("")
from macro.config import config
class keyEvent:
    def __init__(self,part,action,parameters=[]):
        self.action=action
        self.parameters=parameters
        self.part=part
        self.code_id=config.VK_CODE[part]

    def execute(self):
        if self.action=='按下':
            win32api.keybd_event(self.code_id, 0, 0, 0)
            if self.parameters:
                t=kb_timer(threading.Event(),int(self.parameters[0]),self.part,'松开')
                t.start()
                

        elif self.action=='松开':
            win32api.keybd_event(self.code_id, 0, win32con.KEYEVENTF_KEYUP, 0)

class kb_timer(threading.Thread):
    def __init__(self,event,delay,part,action):
        self.part=part
        self.action=action
        self.delay=delay
        self.event=event
        self.event.set()
        super(kb_timer,self).__init__()

    def run(self):
        sleep(self.delay/1000)
        ke=keyEvent(self.part,self.action,[])
        ke.execute()
