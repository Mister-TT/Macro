#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from win32 import win32api
from win32.lib import win32con
from win32 import win32gui
from pythonwin import win32ui
import sys
sys.path.append("")

from macro.modules.tech.function import *
from macro.config import config
scale = 1

class Image_recognize():
    def __init__(self):
        pass

    def recognize(self, small_url, big_url = "", debug = True):
        
        if(big_url == ""):
            window_capture("./cache/screenshot.jpg")
            low_image("./cache/screenshot.jpg", 1920, 1080, "./cache/screenshot.jpg")
            big_url = "./cache/screenshot.jpg"
        
        self.img = cv2.imdecode(np.fromfile(big_url, dtype=np.uint8), -1)
        self.img = cv2.resize(self.img, (0, 0), fx=scale, fy=scale)

        self.template = cv2.imdecode(np.fromfile(small_url, dtype=np.uint8), -1)
        self.template = cv2.resize(self.template, (0, 0), fx=scale, fy=scale)
        self.template_size = self.template.shape[:2]

        self.img, x_, y_ = self.search_returnPoint(self.img, self.template, self.template_size)
        
        if(self.img is None):
            print("没找到图片")
            return [-10, -10]
        elif(debug == True):
            print("找到图片 位置:"+str(x_)+" " + str(y_))
            plt.figure()
            plt.imshow(self.img, animated=True)
            plt.show()
        return [x_, y_]

    def search_returnPoint(self, img, template, template_size):
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


if __name__ == "__main__":
    obj = Image_recognize()
    # big = "C:\\myProject\\Macro\\Work\\macro\\modules\\tech\\img\\big.jpg"
    small = "C:\\Users\\86137\\Desktop\\ABC.jpg"
    obj.recognize(small)
