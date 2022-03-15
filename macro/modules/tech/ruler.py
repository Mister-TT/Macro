#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# from macro.modules.tech.file import file
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.image as image
import time


class ruler():
    def __init__(self):
        self.fig, self.img = plt.subplots()
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)
       
    def showRuler(self):
        plt.ion()
        try:
            self.img = image.imread("./cache/screenshot.jpg")  # 主展示
            self.another_img = cv2.imread("./cache/screenshot.jpg")  # 备份
        except FileNotFoundError:
            print("没找到目标文件：" + "./cache/screenshot.jpg")
            return -1
        
        manager = plt.get_current_fig_manager()
        manager.window.showMaximized()

        plt.clf()
        plt.imshow(self.img)
        plt.ioff()

        plt.show()
        plt.ion()
    # def used(self, filepath):

    def onclick(self, event):
        # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        #     ('double' if event.dblclick else 'single', event.button,
        #     event.x, event.y, event.xdata, event.ydata))
        # t = time.time()
        plt.ion()
        x = int(event.xdata)
        y = int(event.ydata)
        xy = "%d,%d" % (x, y)
        cv2.circle(self.another_img, (x, y), 2, (255, 0, 255), thickness=2)
        if(y > 1000):
            cv2.putText(self.another_img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                        3.0, (0, 255, 0), thickness=1)
        else:
            cv2.putText(self.another_img, xy, (x, y + 35), cv2.FONT_HERSHEY_PLAIN,
                        3.0, (0, 255, 0), thickness=1)

        # print(time.time() - t)

        # t = time.time()
        cv2.imwrite('./cache/screenshot.jpg', self.another_img)
        # print(time.time() - t)

        # t = time.time()
        self.img = image.imread('./cache/screenshot.jpg')
        # print(time.time() - t)

        # t = time.time()
        self.another_img = cv2.imread('./cache/screenshot.jpg')
        # print(time.time() - t)

        # t = time.time()
        plt.clf()
        plt.imshow(self.img)
        # print(time.time() - t)

        # print("\n")
        # plt.ioff()
        # plt.show()
        # plt.imshow(self.img)

if __name__ == "__main__":
    obj = ruler()
    obj.run()
    # use_ruler("123.jpg")
    # use_ruler("123.jpg")
