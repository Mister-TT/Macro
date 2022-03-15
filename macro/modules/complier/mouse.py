from win32 import win32api
from win32.lib import win32con
from win32 import win32gui
from pythonwin import win32ui
import threading
from time import sleep
class mouseEvent():
    def __init__(self,action,parameters):
        self.action=action
        self.parameters=parameters
        self.sw = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        self.sh = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    def execute(self):
        if self.action=='移动到':
            x,y=self.parameters
            nx = int(int(x) * 65535 / self.sw)
            ny = int(int(y) * 65535 / self.sh)
            if nx>=0 and ny>=0:
                win32api.mouse_event(
                    win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE, nx, ny, 0, 0)

        elif self.action=='左键点击':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        elif self.action=='右键点击':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

        elif self.action=='中键点击':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)

        elif self.action=='左键按下':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            if self.parameters:
                t=mouse_timer(threading.Event(),int(self.parameters[0]),'左键松开')
                t.start()

        elif self.action=='右键按下':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            if self.parameters:
                t=mouse_timer(threading.Event(),int(self.parameters[0]),'右键松开')
                t.start()

        elif self.action=='中键按下':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0)
            if self.parameters:
                t=mouse_timer(threading.Event(),int(self.parameters[0]),'中键松开')
                t.start()

        elif self.action=='左键松开':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            
        elif self.action=='右键松开':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

        elif self.action=='中键松开':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0)

        elif self.action=='左键双击':
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            sleep(0.3)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        elif self.action=='下滚轮':
            x=int(self.parameters[0])
            win32api.mouse_event(
                win32con.MOUSEEVENTF_WHEEL, 0, 0, -x)

        elif self.action=='上滚轮':
            x=int(self.parameters[0])
            win32api.mouse_event(
                win32con.MOUSEEVENTF_WHEEL, 0, 0, x)

        elif self.action=='左键拖动':
            sx,sy,tx,ty=self.parameters
            sx = int(int(sx) * 65535 / self.sw)
            sy = int(int(sy) * 65535 / self.sh)
            tx = int(int(tx) * 65535 / self.sw)
            ty = int(int(ty) * 65535 / self.sh)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE,sx, sy, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE,tx, ty, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        elif self.action=='右键拖动':
            sx,sy,tx,ty=self.parameters
            sx = int(int(sx) * 65535 / self.sw)
            sy = int(int(sy) * 65535 / self.sh)
            tx = int(int(tx) * 65535 / self.sw)
            ty = int(int(ty) * 65535 / self.sh)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE,sx, sy, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE,tx, ty, 0, 0)
            win32api.mouse_event(
                win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)

class mouse_timer(threading.Thread):
    def __init__(self,event,delay,action):
        self.action=action
        self.delay=delay
        self.event=event
        self.event.set()
        super(mouse_timer,self).__init__()

    def run(self):
        sleep(self.delay/1000)
        me=mouseEvent(self.action,[])
        me.execute()

        
