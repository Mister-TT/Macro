#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2018-12-02 19:04:55
import sys
sys.path.append("")

import wave
import time
import json

IS_PY3 = sys.version_info.major == 3

if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode

    timer = time.perf_counter
else:
    import urllib2
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

    if sys.platform == "win32":
        timer = time.clock
    else:
        # On most other platforms the best timer is time.time()
        timer = time.time

from pyaudio import PyAudio, paInt16
from macro.config import config



class voiceManager():
    framerate = 16000  # 采样率
    num_samples = 2000  # 采样点
    channels = 1  # 声道
    sampwidth = 2  # 采样宽度2bytes
    FILEPATH = './cache/speech.wav'

    FORMAT = FILEPATH[-3:]  # 文件后缀只支持 pcm/wav/amr 格式，极速版额外支持m4a 格式
    CUID = '123456PYTHON'
    RATE = 16000  # 采样率，固定值

    DEV_PID = 1537  # 1537 表示识别普通话，使用输入法模型。根据文档填写PID，选择语言及识别模型
    ASR_URL = 'http://vop.baidu.com/server_api' # 请求的URL

    def __init__(self):
        self.PyAudioHandler = PyAudio()
        self.state = config.VOICE_RECORD_STOP

    def setVoiceThreading(self, voiceThreading):
        self.voiceThreading = voiceThreading

    def saveWavFile(self, filepath, data):
        wf = wave.open(filepath, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.sampwidth)
        wf.setframerate(self.framerate)
        wf.writeframes(b''.join(data))
        wf.close()

    def myVoiceRecord(self):
        stream = self.PyAudioHandler.open(format=paInt16, channels=self.channels,
                        rate=self.framerate, input=True, frames_per_buffer=self.num_samples)
        my_buf = []

        t = time.time()
        print('正在录音...')
        
        lasttime =  15
        if(self.voiceThreading != None):
            self.voiceThreading.sinOut.emit("剩余录制时间 15" + "s")
        
        while (time.time() < t + 15  and self.state == config.VOICE_RECORD_RECORDING):  # 秒
            tmptime = (15 - (time.time() - t))
            if(lasttime - tmptime >= 1.0):
                if(self.voiceThreading != None):
                    self.voiceThreading.sinOut.emit("剩余录制时间 %d" % (tmptime + 1) + "s")
                lasttime = tmptime
            string_audio_data = stream.read(self.num_samples)
            my_buf.append(string_audio_data)
        print('录音结束.')
        
        self.saveWavFile(self.FILEPATH, my_buf)
        stream.close()

    def changeVoiceManagerState(self):
        if(self.state == config.VOICE_RECORD_RECORDING):
            self.state = config.VOICE_RECORD_STOP
        elif(self.state == config.VOICE_RECORD_STOP):
            self.state = config.VOICE_RECORD_RECORDING

    def getState(self):
        return self.state

    def myVoiceRecognize(self):
        token = "24.5cbcc7626eb690815f86b3650ad96ee3.2592000.1622115342.282335-15803531"

        """
        httpHandler = urllib2.HTTPHandler(debuglevel=1)
        opener = urllib2.build_opener(httpHandler)
        urllib2.install_opener(opener)
        """

        speech_data = []
        try:
            with open(self.FILEPATH, 'rb') as speech_file:
                speech_data = speech_file.read()
        except FileNotFoundError:
            return "--"

        length = len(speech_data)
        if length == 0:
            print('file %s length read 0 bytes' % self.FILEPATH)

        params = {'cuid': self.CUID, 'token': token, 'dev_pid': self.DEV_PID}
        #测试自训练平台需要打开以下信息
        #params = {'cuid': CUID, 'token': token, 'dev_pid': DEV_PID, 'lm_id' : LM_ID}
        params_query = urlencode(params)

        headers = {
            'Content-Type': 'audio/' + self.FORMAT + '; rate=' + str(self.RATE),
            'Content-Length': length
        }

        # url = ASR_URL + "?" + params_query
        req = Request(self.ASR_URL + "?" + params_query, speech_data, headers)
        try:
            f = urlopen(req)
            result_str = f.read()
        except URLError as err:
            return "--"
            print('asr http response http code : ' + str(err.code))
            result_str = err.read()

        if (IS_PY3):
            result_str = str(result_str, 'utf-8')

        result_str = json.loads(result_str)
        if(result_str['err_msg'] == 'success.'):
            print("语音识别结果为：" + result_str['result'][0])
            return result_str['result']
        else:
            print("语音识别错误, 错误类型为: " + result_str['err_msg'])
            return "--"



if __name__ == '__main__':
    obj = voiceManager(None)
    # obj.changeVoiceManagerState()
    obj.my_voice_recognize()