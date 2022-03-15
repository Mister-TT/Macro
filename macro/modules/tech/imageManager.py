#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time
from PyQt5.QtWidgets import QApplication
import sys
sys.path.append("")

from PIL import Image, ImageGrab
import pytesseract
import re
import base64
import requests
from macro.config import config
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from win32 import win32gui
from win32.lib import win32con

class imageManager():
    def __init__(self):
        self.scale = 1
        self.access_token = '24.28952c4d77d6a472f20f0b021619f184.2592000.1624796251.282335-24078826'
        # access_token = "24.0c1b45d3e99f790fa06ef4502f5f3246.2592000.1623070393.282335-24131970"
        self.headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
        self.request_url = self.request_url + "?access_token=" + self.access_token
    
    def showWindow(self,SW = win32con.SW_SHOWNORMAL, window = "Macro", cx = 1200, cy = 900):
        hwnd = win32gui.FindWindow(None, window)
        if(SW == win32con.SW_SHOWNORMAL or SW == win32con.SW_MAXIMIZE):
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0,0,cx,cy, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE)
        win32gui.ShowWindow(hwnd, SW)

    def window_capture(self, imagePath):
        im = ImageGrab.grab()
        im.save(imagePath)

    def low_image(self, file_in, width, height, file_out):
        try:
            image = Image.open(file_in)
            resized_image = image.resize((width, height), Image.ANTIALIAS)
            resized_image.save(file_out)
        except FileNotFoundError:
            print("未找到照片，无法降低像素")
            return -1

    def __getMyScreenShot(self):
        self.window_capture("./cache/screenshot.jpg")
        self.low_image("./cache/screenshot.jpg", 1920,
                         1080, "./cache/screenshot.jpg")
        return "./cache/screenshot.jpg"

    def __searchReturnPoint(self, img, template, template_size):
        img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        template_ = cv2.cvtColor(self.template, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(img_gray, template_, cv2.TM_CCOEFF_NORMED)
        threshold = config.IMAGE_ACCURACY * 0.01
        # res大于70%
        loc = np.where(result >= threshold)
        # 使用灰度图像中的坐标对原始RGB图像进行标记
        point = ()

        for pt in zip(*loc[::-1]):
            cv2.rectangle(self.img, pt, (pt[0] + template_size[1],
                                         pt[1] + + template_size[0]), (7, 249, 151), 2)
            point = pt
        if point == ():
            return None, None, None
        return img, point[0] + template_size[1] / 2, point[1] + template_size[0] / 2

    def mkdir(folderpath):
        folder = os.path.exists(folderpath)
        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(folderpath)  # makedirs 创建文件时如果路径不存在会创建这个路径

    def findSmallImage(self, smallPath, bigPath = "", debug = True):
        if(bigPath == ""):
            bigPath = self.__getMyScreenShot()

        self.img = cv2.imdecode(np.fromfile(bigPath, dtype=np.uint8), -1)
        self.img = cv2.resize(self.img, (0, 0), fx=self.scale, fy=self.scale)

        self.template = cv2.imdecode(
            np.fromfile(smallPath, dtype=np.uint8), -1)
        self.template = cv2.resize(self.template, (0, 0), fx=self.scale, fy=self.scale)
        self.template_size = self.template.shape[:2]

        self.img, x_, y_ = self.__searchReturnPoint(
            self.img, self.template, self.template_size)

        if(self.img is None):
            print("没找到图片")
            return [-10, -10]
        elif(debug == True):
            print("找到图片 位置:"+str(x_)+" " + str(y_))
            plt.figure()
            plt.imshow(self.img, animated=True)
            plt.show()
        return [x_, y_]

    def OCR_FindWord_Baidu(self, word, imagePath = ""): # 用了百度技术
        if(imagePath == ""):
            imagePath = self.__getMyScreenShot()

        f = open(imagePath, 'rb')
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(
            self.request_url, data=params, headers=self.headers)

        print(response.json())
        try:
            for item in (response.json())['words_result']:
                # print(item)
                if(re.match(word, item['words'], flags=0) != None):
                    x = item['location']['left'] + \
                        item['location']['width'] / 2
                    y = item['location']['top'] + \
                        item['location']['height'] / 2
                    return [x, y]
        except KeyError:
            return [-10, -10]
        return [-10, -10]

    def OCR_RecognizehWord_Py(self, imagePath): # 用了pytesseract技术
        text = pytesseract.image_to_string(Image.open(
            imagePath), lang='eng')
        return text

if __name__ == "__main__":
    obj = imageManager()
    obj.OCR_FindWord_Baidu("123321", "C:\\myProject\\UML\\Work\\cache\\12.jpg")
    # obj.findSmallImage("C:\\myProject\\UML\\Work\\cache\\small.jpg")
    # print("Hello")
