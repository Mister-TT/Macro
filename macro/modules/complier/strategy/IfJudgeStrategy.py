import re
import sys
sys.path.append("")
from macro.modules.complier.strategy import JudgeStrategy
from macro.modules.complier import Grammar
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier.expressionjudger import BooleanExpressionJudger

from macro.modules.complier.pool import VarPool


class IfJudgeStrategy(JudgeStrategy.JudgeStrategy):
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance   

    ifCount=0
    elseCount=0
    def __init__(self):
        JudgeStrategy.JudgeStrategy.__init__(self)
        self.__ifCommandList=self._grammar.getIfCommandList()
        self.__parameterofIfCommandList=self._grammar.getParameterofIfCommandList()
        self.__expJudger=ExpressionJudgerStrategy.ExpressionJudgerStrategy()       

    def reset(self):
        self.ifCount=0
        self.elseCount=0


    def judge(self,command):
        now1=0
        for line1 in self.__ifCommandList:
            if(self.__parameterofIfCommandList[now1].__len__()==0):          
                if(re.match(line1,command)):
                    self.ifCount+=self._grammar.ifMapping(line1)
                    self.elseCount+=self._grammar.elseMapping(line1)
                    if(self._grammar.ifMapping(line1)==-1 or self._grammar.ifMapping(line1)==1):
                        self.elseCount=self.ifCount
                    if(self.ifCount>self.elseCount):
                        self._exp='没有if语句对应的else'
                        return False
                    return True

                now1+=1
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
           
                if(tempList.__len__()!=self.__parameterofIfCommandList[now1].__len__()):
                    self._exp='参数数量错误'
                    return False
                self.__expJudger=BooleanExpressionJudger.BooleanExpressionJudger()
                for now2 in range(0,tempList.__len__()):
                    if(self.__parameterofIfCommandList[now1][now2]=='布尔表达式'):
                        if(not self.__expJudger.judge(tempList[now2])):
                            self._exp='表达式出现错误'
                            return False 

                self.ifCount+=self._grammar.ifMapping(line1)
                self.elseCount+=self._grammar.elseMapping(line1)
                if(self._grammar.ifMapping(line1)==-1 or self._grammar.ifMapping(line1)==1):
                    self.elseCount=self.ifCount
                if(self.ifCount>self.elseCount):
                    self._exp='没有if语句对应的else'
                    return False
 
                return True           
            now1+=1

        return False

    def isIfFinished(self):

        return self.ifCount==0



