import datetime
import array
import time
import sys
import os
import re
sys.path.append("")


from macro.config import config
from PyQt5.QtWidgets import QFileDialog

class fileManager():
    def __init__(self):
        try:
            self.fd = open('./cache/test.txt', 'w',  encoding='utf-8')
            self.fd.close()
            os.remove('./cache/test.txt')
        except FileNotFoundError:
            pass

    def controllerOpen(self):
        filename = QFileDialog.getOpenFileName(
            None, 'open file', "./scripts", "Text Files(*.txt)")
        return filename[0] 

    def controllerSave(self):
        filename = QFileDialog.getSaveFileName(None,'save file','',"文本文件(*.txt)")
        return filename[0]

    def controllerImageFile(self):
        QFileDialog.getOpenFileName(None, 'open file', "./img", "Image Files(*.jpg *.png)")

    def newPage(self):
        pass

    def remove(self, filepath):
        if(config.TMP_FILE_PATH == filepath):
            return False
        os.remove(filepath)
        return True

    def search(self, keyWord):
        rgx = re.compile('.*'.join(re.escape(x) for x in keyWord))
        need = []
        for name in os.listdir(config.TMP_DIR + "/scripts"):    
            if(re.search(rgx, name, 0) != None):
                need.append(name)
        return need

    def open(self, path):
        self.fd = open(path, 'a', encoding='utf-8')
        
    def output(self, content_array):
        try:
            for string in content_array:
                self.output_once(string)
        except ValueError:
            print("不能在已经关闭的文件里进行书写")

    def output_once(self, content):
        print(content, file=self.fd)
        
    def close(self):
        self.fd.close()

    def get_script_path(self, script):
        path = os.path.join(os.getcwd(), 'scripts', script)
        print(path)
        return path

    def new_script_path(self, form):
        now = datetime.datetime.now()
        script = '%s.' % now.strftime('%m%d_%H%M%S') + form
        return self.get_script_path(script)
 
    def mkdir(self, path):
        folder = os.path.exists(path)
        if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
    
    def hookWriteEvent(self, content, outpath, lastTime):
        self.open(outpath)
        self.output(["\n"])

        new_content = []
        deadline = lastTime - config.DELETE_TIME_ACCURACY
        for line in content:
            print(line[0])
            if(line[1] < deadline):
                new_content.append(line[0])
        self.output(new_content)
        self.close()

if __name__ == "__main__":
    obj = fileManager()
    # print(obj.get_script_path("123"))
    # obj.mkdir("132")
    

