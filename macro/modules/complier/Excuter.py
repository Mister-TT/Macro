from pythonwin import win32ui
from win32 import win32gui
from win32.lib import win32con
from win32 import win32api
import pyperclip
import sys
sys.path.append("")

import threading
from time import sleep
from macro.modules.complier.mouse import mouseEvent
from macro.modules.complier.keyboard import keyEvent
from macro.modules.complier import Transfer
#from macro.modules.tech.image_recognize import Image_recognize
from macro.modules.tech.image_word import Image_word
from macro.modules.tech.imageManager import imageManager
from PyQt5.QtCore import QThread, pyqtSignal
from macro.config import config
from os import path
from macro.logs import logger
from PIL import ImageGrab
from PIL import Image
import re


# 跑脚本的时候是用下面这个
class Excuter():


    def __init__(self):
        self.if_flag=[]
        self.if_state=[]
        self.whlie_state=[]
        self.while_pos=[]
        self.continue_flag=0
        self.variable={}
        self.priority={}
        self.priority['(']=20
        self.priority[')']=20
        self.priority['+']=12
        self.priority['-']=12
        self.priority['*']=13
        self.priority['/']=13
        self.priority['>']=7
        self.priority['<']=7
        self.priority['==']=7
        self.priority['!=']=7
        self.priority['>=']=7
        self.priority['<=']=7
        self.priority['pic_in']=5
        self.priority['words_in']=5
        self.priority['not']=4
        self.priority['and']=3
        self.priority['or']=2


    def excute(self, userCommandList, thd = None):
        script=Transfer.Transfer()
        script.transfer(userCommandList)
        steps=script.getTop()
        i=0
        while i<steps:
            if config.IS_RUNNING==0:
                print("断了")
                break

            equipment=script.getEquipment()[i]
            part=script.getPart()[i]
            action=script.getAction()[i]
            parameters=script.getParamters()[i]
            
            if not self.__checkIf(equipment,parameters):
                i=i+1
                continue

            pos=self.__checkWhile(equipment,i,parameters)
            if pos==-1:
                i=i+1
                continue
            elif pos>=0:
                i=pos
                continue

            if equipment == '鼠标':      
                if part+action=='移动到': 
                    objw=Image_word()
                    obj=imageManager()
                    if parameters[0]=='坐标':
                        parameters=parameters[1:]
                    elif parameters[0]=='小图截屏':
                        print(self.variable[parameters[1]][1])
                        parameters=obj.findSmallImage(smallPath=self.variable[parameters[1]][1],debug=False)
                    elif parameters[0]=='小图大图':
                        parameters=obj.findSmallImage(smallPath=self.variable[parameters[1]][1],bigPath=self.variable[parameters[2]][1],debug=False)
                    elif parameters[0]=='文字截屏':
                        parameters=obj.OCR_FindWord_Baidu(word=parameters[1])
                    elif parameters[0]=='文字大图':
                        parameters=obj.OCR_FindWord_Baidu(word=parameters[1],imagePath=self.variable[parameters[2]][1])

                me=mouseEvent(part+action,parameters)
                me.execute()

            elif equipment=='键盘':
                ke=keyEvent(part,action,parameters)
                ke.execute()

            elif equipment=='':
                if action=='延迟':
                    try:
                        delay=self.cal_all(parameters)[1]/1000
                        sleep(delay)
                    except TypeError:
                        logger.error("延迟函数错误")

            elif equipment=='打印':
                print("Hello World" + parameters[0])
                thd.sinOut.emit(parameters[0])

            elif equipment=='输出':
                thd.sinOut.emit(str(self.cal_all(parameters)[1]))

            elif equipment=='连点器':
                self.__holdClick(part+action,parameters)

            elif equipment=='等待图':
                self.__waitImg(parameters[0])

            elif equipment=='定义':
                if action=='字符串':
                    self.variable[part]=['字符串',parameters[0]]
                elif action=='图片':
                    self.variable[part]=['图片',self.find_imgpath(parameters[0])]
                elif action=='整型' or action=='布尔型':
                    if len(parameters)==1:
                        self.__createVariable(part,[action,parameters[0]])
                    else:              
                        if parameters[0]=='画面':
                            self.__recognizeNum(part,parameters)
                        else:
                            self.variable[part]=self.cal_all(parameters)                       
                    
                print(part,self.variable[part])

            elif equipment=='令':
                kind=self.variable[part][0]
                if kind=='整型' or kind=='布尔型':
                    if parameters[0]=='画面':
                        self.__recognizeNum(part,parameters)
                    else:
                        self.variable[part]=self.cal_all(parameters)
                elif kind=='图片':
                    self.variable[part]=['图片',self.find_imgpath(parameters[0])]
                elif kind=='字符串':
                    self.variable[part]=parameters[0]
                print(part,self.variable[part])         


            i=i+1

    def __waitImg(self,name):
        imgpath=self.transfer_to_list(name)
        obj=imageManager()
        pos=[-10,-10]
        while pos[0]<0 or pos[1]<0:
            pos=obj.findSmallImage(smallPath=imgpath[1],debug=False)
        me=mouseEvent('移动到',pos)
        me.execute()

    def __recognizeNum(self,part,parameters):
        self.__imgShot(parameters)
        obj=imageManager()
        num=obj.OCR_FindWord_Baidu(self.tmp_img_path())
        if num=='!':
            self.sinOut.emit('无法识别数字')
        else:
            num=re.findall(r'\d+',num)
            if num==[]:
                self.sinOut.emit('无法识别数字')
                self.variable[part]=['整型',0]
            else:
                self.variable[part]=['整型',num[0]]

    def __holdClick(self,part,parameters):
        p=self.__handleExpression(parameters)
        a1=self.cal_all(p[0])
        a2=self.cal_all(p[1])
        a3=self.cal_all(p[2])
        a4=self.cal_all(p[3])
        for i in range(a1[1]):
            me=mouseEvent('移动到',[a2[1],a3[1]])
            me.execute()
            me=mouseEvent(part+'点击',[])
            me.execute()
            sleep(a4[1]/1000)

    def tmp_img_path(self):
        tmp_path=path.dirname(__file__)
        for i in range(3):
            tmp_path=path.dirname(tmp_path)
        tmp_path+='\\cache\\tmp_img.png'
        return tmp_path

    def __handleExpression(self,parameters):
        p=[]
        st=0
        for i in range(0,len(parameters)-1):
            isnum1=not parameters[i] in self.priority
            isnum2=not parameters[i+1] in self.priority
            if isnum1 and isnum2:
                p.append(parameters[st:i+1])
                st=i+1
        p.append(parameters[st:])
        return p

    @logger.catch(reraise=True)
    def __imgShot(self,parameters):
        p=self.__handleExpression(parameters[1:])

        x1=self.cal_all(p[0])
        y1=self.cal_all(p[1])
        x2=self.cal_all(p[2])
        y2=self.cal_all(p[3])
        im=ImageGrab.grab((x1[1],y1[1],x2[1],y2[1]))     
        im.save(self.tmp_img_path())

    def img_exists(self,img_name):
        img_path=self.find_imgpath(img_name)
        return path.isfile(img_path)

    def find_imgpath(self,img_name):
        img_path=path.dirname(__file__)
        for i in range(3):
            img_path=path.dirname(img_path)
        img_path+='\\img\\'
        img_path+=img_name
        # print(img_path)
        return img_path

    def __checkIf(self,equipment,parameters):
        if equipment=='如果':
            if self.cal_all(parameters)[1]:
                self.if_flag.append(1)
            else:
                self.if_flag.append(0)

        elif equipment=='那么':
            self.if_state.append(1)

        elif equipment=='否则':
            self.if_state.pop(-1)
            self.if_state.append(0)

        elif equipment=='条件结束':
            self.if_flag.pop(-1)
            self.if_state.pop(-1)

        elif self.if_flag==self.if_state:
            return True

        return False      

    def __checkWhile(self,equipment,pos,parameters):
        if equipment=='当':
            if self.cal_all(parameters)[1]:
                self.whlie_state.append(1)
            else:
                self.whlie_state.append(0)
            self.while_pos.append(pos)

        elif equipment=='循环结束':
            self.continue_flag=0
            if 0 in self.whlie_state:
                self.whlie_state.pop(-1)
                self.while_pos.pop(-1)
                return -1
            else:
                val=self.while_pos[-1]
                self.whlie_state.pop(-1)
                self.while_pos.pop(-1)
                return val
                
        elif equipment=='循环开始':
            self.whlie_state.append(1)
            self.while_pos.append(pos)

        elif equipment=='直到':
            self.continue_flag=0
            if self.cal_all(parameters)[1]:
                if 0 in self.whlie_state:
                    self.whlie_state.pop(-1)
                    self.while_pos.pop(-1)
                    return -1
                else:
                    val=self.while_pos[-1]
                    self.whlie_state.pop(-1)
                    self.while_pos.pop(-1)
                    return val
            else:
                self.whlie_state.pop(-1)
                self.while_pos.pop(-1)
                return -1

        elif self.continue_flag==1 or 0 in self.whlie_state:
            return -1

        elif equipment=='退出循环':
            self.whlie_state[-1]=0

        elif equipment=='继续':
            self.continue_flag=1

        elif equipment=='退出所有循环':
            for x in range(len(self.whlie_state)):
                self.whlie_state[x]=0

        

        return -2

    def __createVariable(self,name,val):
        if val[0]=='整型':
            val[1]=int(val[1])
        self.variable[name]=val  

    def transfer_to_list(self,name):
        if isinstance(name,str):
            if name in self.variable:
                return self.variable[name]
            elif name.isdigit():
                return ['整型',int(name)]
            else:
                if name=='true' or name=='false':
                    return ['布尔型',name]
                elif self.img_exists(name):
                    return ['图片',self.find_imgpath(name)]
                else:
                    return ['字符串',name]
        else:
            return name

    def cal_once(self,name1,operator,name2):
        var1=self.transfer_to_list(name1)
        var2=self.transfer_to_list(name2)
     
        if var1[0]=='整型':
            if operator=='+':
                return [var1[0],var1[1]+var2[1]]
            elif operator=='-':
                return [var1[0],var1[1]-var2[1]]
            elif operator=='*':
                return [var1[0],var1[1]*var2[1]]
            elif operator=='/':
                return [var1[0],var1[1]/var2[1]]        
            elif operator=='<':
                return ['布尔型',var1[1]<var2[1]]
            elif operator=='>':
                return ['布尔型',var1[1]>var2[1]]
            elif operator=='<=':
                return ['布尔型',var1[1]<=var2[1]]
            elif operator=='>=':
                return ['布尔型',var1[1]>=var2[1]]
            elif operator=='==':
                return ['布尔型',var1[1]==var2[1]]
            elif operator=='!=':
                return ['布尔型',var1[1]!=var2[1]]
            else:
                print('运算符不合法')
                exit()
        elif var1[0]=='布尔型':    
            if operator=='and':
                return [var1[0],var1[1] and var2[1]]
            elif operator=='or':
                return [var1[0],var1[1] or var2[1]]
            elif operator=='not':
                return [var2[0],not var2[1]]
            elif operator=='==':
                return [var1[0],var1[1]==var2[1]]
            elif operator=='!=':
                return [var1[0],var1[1]!=var2[1]]
            else:
                print('运算符不合法')
        elif var1[0]=='图片':
            if operator=='pic_in':
                obj=imageManager()
                if var2[0]=='图片':
                    pos=obj.findSmallImage(smallPath=var1[1],big_url=var2[1],debug=False)        
                elif var2[0]=='字符串' and var2[1]=='画面':
                    pos=obj.findSmallImage(smallPath=var1[1],debug=False)
                if pos[0]<0 and pos[1]<0:
                        return ['布尔型',False]
                else:
                    return ['布尔型',True]
        elif var1[0]=='字符串':
            if operator=='words_in':
                obj=Image_word()
                if var2[0]=='图片':
                    pos=obj.run(word=var1[1],smallPath=var2[1])
                elif var2[0]=='字符串' and var2[1]=='画面':
                    pos=obj.run(word=var1[1])
                if pos[0]<0 and pos[1]<0:
                        return ['布尔型',False]
                else: 
                    return ['布尔型',True]

        else:
            print('不合法类型试图进行运算')
            exit()

    def to_postfix(self,exp):
        s1=[]
        s2=[]
        for x in exp:
            if x in self.priority:               
                if x=='(':
                    s1.append(x)
                elif x==')':
                    while s1 and s1[-1]!='(':
                        s2.append(s1[-1])
                        s1.pop(-1)
                    s1.pop(-1)
                else:
                    if not s1 or s1[-1]=='(':
                        s1.append(x)                  
                    else:
                        if self.priority[x]>self.priority[s1[-1]]:
                            s1.append(x)
                        else:
                            while s1 and self.priority[x]<=self.priority[s1[-1]]:
                                s2.append(s1[-1])
                                s1.pop(-1)
                            s1.append(x)
            else:
                s2.append(x)
            # print(s1,s2)            
        while s1:
            s2.append(s1[-1])
            s1.pop(-1)
        # print(s2)
        return s2

    def cal_all(self,expression):
        if len(expression)==1:
            val=self.transfer_to_list(expression[0])
            return val
        exp=self.to_postfix(expression)
        stk=[]     
        for x in exp:
            if x in self.priority:
                if x=='not':
                    val=self.cal_once(['布尔型',True],x,stk[-1])
                    stk.pop(-1)
                    stk.append(val)
                else:
                    val=self.cal_once(stk[-2],x,stk[-1])
                    stk.pop(-1)
                    stk.pop(-1)
                    stk.append(val)
            else:
                stk.append(x)
        return val

t = None
def exe_run(path):
    global t
    t=RunScriptClass(path,threading.Event())
    t.sinOut.connect(get_thread_message)
    t.start()

def get_thread_message(content):
    if(content == "lock"):
        config.SUB_UI_HANDLER.lock()
    elif(content == "unlock"):
        config.SUB_UI_HANDLER.unlock()
    else:
        config.SUB_UI_HANDLER.set_exe_sub_window_text(content)
    pass

if __name__ == '__main__':
    bbox = (0, 0, 800, 400)
    im = ImageGrab.grab(bbox)
    # 参数 保存截图文件的路径
    im.save('D:\\SCUT\\hello-world\\cache\\tmp_img.png')
