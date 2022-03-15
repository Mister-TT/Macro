# encoding:utf-8

import requests
import base64
import sys
import os
import re
sys.path.append("")
from macro.modules.tech.function import window_capture, low_image
from macro.config import config

import pytesseract
from PIL import Image

access_token = '24.5df8df24610f4804746a83a527347581.2592000.1622115551.282335-24078826'
# access_token = "24.0c1b45d3e99f790fa06ef4502f5f3246.2592000.1623070393.282335-24131970"
class Image_word():
    def __init__(self):
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}

    def run(self, word, small_url = ""):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
        self.request_url = request_url + "?access_token=" + access_token
        if(small_url == ""):
            window_capture("./cache/screenshot.jpg")
            low_image("./cache/screenshot.jpg", 1920, 1080, "./cache/screenshot.jpg")
            small_url = os.getcwd() + "/cache/screenshot.jpg"
            
        f = open(small_url, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(self.request_url, data=params, headers=self.headers)
        
        res = []
        print(response.json())
        try:
            for item in (response.json())['words_result']:
                # print(item)
                if(re.match(word, item['words'], flags=0) != None):
                    x = item['location']['left'] + item['location']['width'] / 2
                    y = item['location']['top'] + item['location']['height'] / 2
                    return [x, y]
        except KeyError:
            return [-10 , -10]
        return [-10 ,-10]
    
    def number(self, url):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
        self.request_url = request_url + "?access_token=" + access_token
        f = open(url, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(
            self.request_url, data=params, headers=self.headers)

        res = []
        print(response.json())
        try:
            ans = (response.json())['words_result'][0]['words']
        except TypeError:
            return '!'
        return ans
    
    def number2(self, url):
        text = pytesseract.image_to_string(Image.open(
            url), lang='eng')
        return text


if __name__ == "__main__":
    obj = Image_word()
    print(obj.number("C:\\myProject\\Macro\\Work\\45.jpg"))

