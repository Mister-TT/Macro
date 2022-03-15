import sys
sys.path.append("")

from macro.modules.controller.Method.methodInterface import MethodInterface
from macro.modules.tech.voiceManager import voiceManager
from macro.modules.controller.MultiThread import myVoiceThread
from macro.config import config

class voiceMethod(MethodInterface):
    def justDoit(self, controller):
        if(controller.voiceManagerHandler.getState() == config.VOICE_RECORD_STOP):
            controller.voiceManagerHandler.changeVoiceManagerState()
            controller.voiceThreading.start()
        elif(controller.voiceManagerHandler.getState() == config.VOICE_RECORD_RECORDING):
            controller.voiceManagerHandler.changeVoiceManagerState()

