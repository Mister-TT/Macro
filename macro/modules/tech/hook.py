#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from pythonwin import win32ui
from win32 import win32gui
from win32.lib import win32con
from win32 import win32api

import pyWinhook
import time
import sys
import os
import re
sys.path.append("")

from macro.config import config
from macro.logs import logger

# mouse wheel -1下移 1上移 √
# mouse left down 
# mouse left up 
# mouse right down 
# mouse right up 
# mouse move √

class State():
    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass

    @abstractmethod
    def doAction(self, hookController):
        pass

class workingState(State):
    def __init__(self):
        super().__init__()
    
    def doAction(self, hookController):
        print("workingState")
        hookController.windowAnnounce("d" + "开始屏幕录制...")
        hookController.hookState_change_state(self)

class preparingState(State):
    def __init__(self):
        super().__init__()
    
    def doAction(self, hookController):
        print("prepaingState")
        hookController.windowAnnounce("d" + "将要开始屏幕录制...")
        hookController.pushButtonAnnounce(False)
        hookController.record = []
        hookController.hookState_change_state(self)


class waitingState(State):
    def __init__(self):
        super().__init__()
    
    def doAction(self, hookController):
        print("waitingState")
        hookController.hookState_change_state(self)
        hookController.pushButtonAnnounce(True)
        return [hookController.record, hookController.last_time]

class dontRecordState(State):
    def __init__(self):
        super().__init__()

    def doAction(self, hookController):
        hookController.hookState_change_state(self)
        

class hook():
    def __init__(self, monitorFunctionHandler):
        self.hm = pyWinhook.HookManager()

        self.monitorFunctionHandler = monitorFunctionHandler
        

        self.waitingStateHandler = waitingState()
        self.preparingStateHandler = preparingState()
        self.workingStateHandler = workingState()
        self.dontRecordStateHandler = dontRecordState()
        self.state = waitingState()
    
        
        self.last_time = 0

        self.record = []
        self.mapping = {}
        self.pushButtonArrary = []
        self.windowArrary = []
        
        self.mapping["mouse left down"] = "鼠标 左键 按下"
        self.mapping["mouse left up"] = "鼠标 左键 松开"
        self.mapping["mouse right down"] = "鼠标 右键 按下"
        self.mapping["mouse right up"] = "鼠标 右键 松开"
        self.mapping["mouse wheel"] = config.WHEEL
        self.mapping["mouse move"] = config.MOVE

        self.key_board_used = {}
        self.key_board_key = {}

        self.init_key_board()

        def __on_mouse_event(event):
            # print(event)
            # print('MessageName:',event.MessageName)
            # print('Message:',event.Message)
            # print('Time:',event.Time)
            # print('Window:',event.Window)
            # print('WindowName:',event.WindowName)
            # print('Position:',event.Position)
            # print('Wheel:',event.Wheel)
            # print('Injected:',event.Injected)
            # print(event.key())
            # print(event.delta)
            # print(event.wheelDelta)
            # print()
            # print('---')
            if(config.IS_RUNNING == 1):
                return True

            pos = event.Position
            if (isinstance(self.state, workingState) == False):
                self.windowAnnounce("w" + "鼠标 横坐标 %d 纵坐标 %d" % (pos[0], pos[1]))
                return True


            self.tmp_time = self.current_ts()
            delay = self.tmp_time - self.last_time
            message = event.MessageName
            which_state = self.mapping[message]

            if(delay < config.MOUSE_ACCURACY):
                return True

            all_content = "延迟 %d," % delay
            if(delay >= config.DELAY_ACCURACY):
                self.record.append(["延迟 %d" % delay, self.tmp_time])

            if (which_state == config.WHEEL):
                wheel = event.Wheel
                if (wheel == 1):
                    self.record.append(["鼠标 上滚轮 1", self.tmp_time])
                    all_content += "鼠标 上滚轮 1"
                else:
                    self.record.append(["鼠标 下滚轮 1", self.tmp_time])
                    all_content += "鼠标 下滚轮 1"
            elif (which_state == config.MOVE):
                self.record.append(["鼠标 移动到 横坐标 %d 纵坐标 %d" % (pos[0], pos[1]), self.tmp_time])
                all_content += "鼠标 移动到 横坐标 %d 纵坐标 %d" % (pos[0], pos[1])
            else:
                self.record.append([self.mapping[message], self.tmp_time])
                all_content += self.mapping[message]
            
            self.windowAnnounce("w" + all_content)
            self.last_time = self.current_ts()
            return True

        @logger.catch(reraise=True)
        def __on_keyboard_event(event):
            Message = event.Message
            Key = event.Key
            
            if(config.IS_RUNNING == 1):
                if(Key == "Escape"):
                    self.waitingStateHandler.doAction(self)
                    print("终止")
                    config.IS_RUNNING = 0
                return True

            if (isinstance(self.state, workingState) == False):
                if(Message == config.KEY_DOWN or Message == config.KEY_ALT_DOWN):
                    self.windowAnnounce("w" + "键盘 按下 %s 键" % self.key_board_key[Key])
                elif(Message == config.KEY_UP):
                    self.windowAnnounce("w" + "键盘 松开 %s 键" % self.key_board_key[Key])
                return True
            else: 
                # 用快捷键的话不会响应
                if(Key == "Escape"):
                    print("录屏终止")
                    self.monitorFunctionHandler()
                    
                return True
                    
            # print('MessageName:',event.MessageName)          #同上，共同属性不再赘述
            # print('Message:',event.Message)
            # print('Time:',event.Time)
            # print('Window:',event.Window)
            # print('WindowName:',event.WindowName)
            # print('Ascii:', event.Ascii, chr(event.Ascii))   #按键的ASCII码
            # print("Key: ", event.Key)
            # logger.info('Key:' + event.Key)                  #按键的名称
            # print('KeyID:', event.KeyID)                     #按键的虚拟键值
            # print('ScanCode:', event.ScanCode)               #按键扫描码
            # print('Extended:', event.Extended)               #判断是否为增强键盘的扩展键
            # print('Injected:', event.Injected)
            # print('Alt', event.Alt)                          #是某同时按下Alt
            # print('Transition', event.Transition)            #判断转换状态
            # print('---')
            
            self.tmp_time = self.current_ts()
            delay = self.tmp_time - self.last_time
            allcontent = ""
            allcontent += "延迟 %d," % delay
            self.record.append(["延迟 %d" % delay, self.tmp_time])
            
            if(Message == config.KEY_DOWN or Message == config.KEY_ALT_DOWN):
                self.record.append(["键盘 按下 %s 键" % self.key_board_key[Key], self.tmp_time])
                allcontent += "键盘 按下 %s 键" % self.key_board_key[Key]
            elif(Message == config.KEY_UP):
                self.record.append(["键盘 松开 %s 键" % self.key_board_key[Key], self.tmp_time])
                allcontent += "键盘 松开 %s 键" % self.key_board_key[Key]

            self.windowAnnounce("w" + allcontent)
            self.last_time = self.current_ts()
            return True

        self.hm.MouseAll = __on_mouse_event
        self.hm.KeyAll = __on_keyboard_event
        self.hm.HookMouse()
        self.hm.HookKeyboard()

    def current_ts(self):
        return int(time.time() * 1000)

    def init_key_board(self):
        self.key_board_key["Escape"] = "Esc"
        self.key_board_key["F1"] = "F1"
        self.key_board_key["F2"] = "F2"
        self.key_board_key["F3"] = "F3"
        self.key_board_key["F4"] = "F4"
        self.key_board_key["F5"] = "F5"
        self.key_board_key["F6"] = "F6"
        self.key_board_key["F7"] = "F7"
        self.key_board_key["F8"] = "F8"
        self.key_board_key["F9"] = "F9"
        self.key_board_key["F10"] = "F10"
        self.key_board_key["F11"] = "F11"
        self.key_board_key["F12"] = "F12"
        self.key_board_key["Snapshot"] = "PrintScreen"
        self.key_board_key["Insert"] = "Ins"
        self.key_board_key["Delete"] = "Del"
        self.key_board_key["Prior"] = "PgUp"
        self.key_board_key["Next"] = "PgDn"
        self.key_board_key["Home"] = "Home"
        self.key_board_key["End"] = "End"
        self.key_board_key["Oem_3"] = "`"
        self.key_board_key["1"] = "1"
        self.key_board_key["2"] = "2"
        self.key_board_key["3"] = "3"
        self.key_board_key["4"] = "4"
        self.key_board_key["5"] = "5"
        self.key_board_key["6"] = "6"
        self.key_board_key["7"] = "7"
        self.key_board_key["8"] = "8"
        self.key_board_key["9"] = "9"
        self.key_board_key["0"] = "0"
        self.key_board_key["Oem_Minus"] = "-"
        self.key_board_key["Oem_Plus"] = "+"
        self.key_board_key["Back"] = "Backspace"
        self.key_board_key["Numlock"] = "NumLock"
        self.key_board_key["Divide"] = "/"
        self.key_board_key["Multiply"] = "*"
        self.key_board_key["Subtract"] = "-"
        self.key_board_key["Tab"] = "Tab"
        self.key_board_key["Q"] = "q"
        self.key_board_key["W"] = "w"
        self.key_board_key["E"] = "e"
        self.key_board_key["R"] = "r"
        self.key_board_key["T"] = "t"
        self.key_board_key["Y"] = "y"
        self.key_board_key["U"] = "u"
        self.key_board_key["I"] = "i"
        self.key_board_key["O"] = "o"
        self.key_board_key["P"] = "p"
        self.key_board_key["Oem_4"] = "["
        self.key_board_key["Oem_6"] = "]"
        self.key_board_key["Oem_5"] = "\\"
        self.key_board_key["Numpad7"] = "7"
        self.key_board_key["Numpad8"] = "8"
        self.key_board_key["Numpad9"] = "9"
        self.key_board_key["Add"] = "+"
        self.key_board_key["Capital"] = "-" 
        self.key_board_key["A"] = "a"
        self.key_board_key["S"] = "s"
        self.key_board_key["D"] = "d"
        self.key_board_key["F"] = "f"
        self.key_board_key["G"] = "g"
        self.key_board_key["H"] = "h"
        self.key_board_key["J"] = "j"
        self.key_board_key["K"] = "k"
        self.key_board_key["L"] = "l"
        self.key_board_key["Oem_1"] = ";"
        self.key_board_key["Oem_7"] = "'"
        self.key_board_key["Return"] = "Enter"
        self.key_board_key["Numpad4"] = "4"
        self.key_board_key["Numpad5"] = "5"
        self.key_board_key["Numpad6"] = "6"
        self.key_board_key["Lshift"] = "Lshift"
        self.key_board_key["Z"] = "z"
        self.key_board_key["X"] = "x"
        self.key_board_key["C"] = "c"
        self.key_board_key["V"] = "v"
        self.key_board_key["B"] = "b"
        self.key_board_key["N"] = "n"
        self.key_board_key["M"] = "m"
        self.key_board_key["Oem_Comma"] = ","
        self.key_board_key["Oem_Period"] = "."
        self.key_board_key["Oem_2"] = "/"
        self.key_board_key["Rshift"] = "Rshift"
        self.key_board_key["Numpad1"] = "1"
        self.key_board_key["Numpad2"] = "2"
        self.key_board_key["Numpad3"] = "3"
        self.key_board_key["Return"] = "Enter"
        self.key_board_key["Lcontrol"] = "Lcontrol"
        self.key_board_key["Lwin"] = "Lwin"
        self.key_board_key["Space"] = "Space"
        self.key_board_key["Rcontrol"] = "Rcontrol"
        self.key_board_key["Left"] = "Left"
        self.key_board_key["Down"] = "Down"
        self.key_board_key["Right"] = "Right"
        self.key_board_key["Numpad0"] = "0"
        self.key_board_key["Decimal"] = "."
        self.key_board_key["Up"] = "Up"
        self.key_board_key["Clear"] = "Clear"
        self.key_board_key["Lmenu"] = "Alt"
        self.key_board_key["Rmenu"] = "Alt"

    def compilerChangeHookState(self):
        if(isinstance(self.state, waitingState)):
            self.dontRecordStateHandler.doAction(self)

    def change_state(self):
        self.last_time = self.current_ts()  

        if (isinstance(self.state, waitingState)):
            print("等待屏幕录制")
            self.preparingStateHandler.doAction(self)
        elif (isinstance(self.state, preparingState)):
            print("开始屏幕录制")
            self.workingStateHandler.doAction(self)
        elif(isinstance(self.state, workingState)):
            print("结束屏幕录制")
            return self.waitingStateHandler.doAction(self)

    def addPushButtonSubscriber(self, subscriber):
        self.pushButtonArrary.append(subscriber)

    def addWindowSubscriber(self, subscriber):
        self.windowArrary.append(subscriber)

    def windowAnnounce(self, content):
        for item in self.windowArrary:
            item.announce(content)

    def pushButtonAnnounce(self, content):
        for item in self.pushButtonArrary:
            item.setEnabled(content)

    def hookState_change_state(self, newState):
        self.state = newState

    def get_state(self):
        return self.state

if __name__ == '__main__':
    obj = hook(1, 2, 3)

    waitingStateHandler = waitingState()
    waitingStateHandler.doAction(obj)

    preparingStateHandler = preparingState()
    preparingStateHandler.doAction(obj)

    workingStateHandler = workingState()
    workingStateHandler.doAction(obj)
