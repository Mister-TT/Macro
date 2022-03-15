# coding=utf-8

import sys
import json
import time

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

from PyQt5.QtWidgets import QApplication
from PIL import Image
from win32gui import error
import time
import sys
import os


def mkdir(folderpath):
    folder = os.path.exists(folderpath)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(folderpath)  # makedirs 创建文件时如果路径不存在会创建这个路径

def low_image(file_in, width, height, file_out):
    try:
        image = Image.open(file_in)
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        resized_image.save(file_out)
    except FileNotFoundError:
        print("未找到照片，无法降低像素")
        return -1

def window_capture(folderpath, filename):
    screen=QApplication.primaryScreen()
    pix=screen.grabWindow(QApplication.desktop().winId())
    mkdir(folderpath)
    pix.save(folderpath + '/' + filename)



TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有

def fetch_token(API_KEY, SECRET_KEY, ):
    params = {'grant_type': 'client_credentials',
            'client_id': API_KEY,
            'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    if (IS_PY3):
        result_str = result_str.decode()

    # print(result_str)
    result = json.loads(result_str)
    # print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        # SCOPE = False 忽略检查
        if SCOPE and (not SCOPE in result['scope'].split(' ')):
            print('scope is not correct')
        # print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' %
            # (result['access_token'], result['expires_in']))
        print(result['access_token'])
        return result['access_token']
    else:
        print('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window_capture("./cache/screenshot1.jpg")
