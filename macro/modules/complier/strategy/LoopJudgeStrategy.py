import re
import sys
sys.path.append("")
from macro.modules.complier.strategy import JudgeStrategy
from macro.modules.complier import Grammar
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier.expressionjudger import ArithmeticExpressionJudger
from macro.modules.complier.expressionjudger import PicturesExpressionJudger
from macro.modules.complier.expressionjudger import BooleanExpressionJudger
from macro.modules.complier.expressionjudger import StringExpressionJudger
from macro.modules.complier.pool import VarPool


class LoopJudgeStrategy(JudgeStrategy.JudgeStrategy):
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance   

    loop1Count=0
    loop2Count=0
    def __init__(self):
        JudgeStrategy.JudgeStrategy.__init__(self)
        self.__loopCommandList=self._grammar.getLoopCommandList()
        self.__parameterofLoopCommandList=self._grammar.getParameterofLoopCommandList()
        self.__expJudger=ExpressionJudgerStrategy.ExpressionJudgerStrategy()       

    def reset(self):
        self.loop1Count=0
        self.loop2Count=0


    def judge(self,command):
        now1=0
        for line1 in self.__loopCommandList:
            if(self.__parameterofLoopCommandList[now1].__len__()==0):          
                if(re.match(line1,command)):
                    self.loop1Count+=self._grammar.loop1Mapping(line1)
                    self.loop2Count+=self._grammar.loop2Mapping(line1)
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
                if(tempList.__len__()!=self.__parameterofLoopCommandList[now1].__len__()):
                    self._exp='参数数量错误'
                    return False
                self.__expJudger=BooleanExpressionJudger.BooleanExpressionJudger()
                for now2 in range(0,tempList.__len__()):
                    if(self.__parameterofLoopCommandList[now1][now2]=='布尔表达式'):
                        if(not self.__expJudger.judge(tempList[now2])):
                            self._exp='表达式出现错误'
                            return False  
                self.loop1Count+=self._grammar.loop1Mapping(line1)
                self.loop2Count+=self._grammar.loop2Mapping(line1)
 
                return True           
            now1+=1

        return False

    def isLoopFinished(self):

        return self.loop1Count==0 and self.loop2Count==0



