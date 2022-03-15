import re
import sys
sys.path.append("")
from macro.modules.complier.strategy import JudgeStrategy
from macro.modules.complier import Grammar

from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier.expressionjudger import ArithmeticExpressionJudger
from macro.modules.complier.expressionjudger import PicturesExpressionJudger
from macro.modules.complier.expressionjudger import KeyExpressionJudger
from macro.modules.complier.pool import KeyPool


class ActionJudgeStrategy(JudgeStrategy.JudgeStrategy):
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance  
        
    def __init__(self):
        JudgeStrategy.JudgeStrategy.__init__(self)
        self.__actionCommandList=self._grammar.getActionCommandList()
        self.__parameterofActionCommandList=self._grammar.getParameterofActionCommandList()
    def judge(self,command):
        now1=0
        
        for line1 in self.__actionCommandList:
            if(self.__parameterofActionCommandList[now1].__len__()==0):
                if(line1==command):
                    return True
                continue

            if(re.match(line1,command)):
                tempList=[]
                temp=[]
                temp=(re.findall(line1,command))
                
                if(isinstance(temp[0],str)):
                    tempList=temp
                else:
                    for line in temp[0]:
                        tempList.append(line)
                if(tempList.__len__()!=self.__parameterofActionCommandList[now1].__len__()):
                    self._exp='参数数量错误'
                    return False
                now2=0
                for line2 in self.__parameterofActionCommandList[now1]:
                    if (line2=='算术表达式'):
                        self.__expJudger=ArithmeticExpressionJudger.ArithmeticExpressionJudger()

                    elif (line2=='图片表达式'):
                        self.__expJudger=PicturesExpressionJudger.PicturesExpressionJudger()

                    elif (line2=='按键'):
                        self.__expJudger=KeyExpressionJudger.KeyExpressionJudger()

                    if(not self.__expJudger.judge(tempList[now2])):
                        self._exp='表达式出现错误'
                        return False   
                    now2+=1

                return True
            now1+=1
        return True



