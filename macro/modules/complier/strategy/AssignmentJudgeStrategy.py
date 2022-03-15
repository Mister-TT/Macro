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


class AssignmentJudgeStrategy(JudgeStrategy.JudgeStrategy):
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance 

    def __init__(self):
        JudgeStrategy.JudgeStrategy.__init__(self)
        self.__assignCommandList=self._grammar.getAssignCommandList()
        self.__parameterofAssignCommandList=self._grammar.getParameterofAssignCommandList()
        self.__expJudger=ExpressionJudgerStrategy.ExpressionJudgerStrategy()       
        self.__varPool=VarPool.VarPool()
    def judge(self,command):
        now1=0
        
        for line1 in self.__assignCommandList:
            if(self.__parameterofAssignCommandList[now1].__len__()==0):
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
                if(tempList.__len__()!=self.__parameterofAssignCommandList[now1].__len__()):
                    self._exp='参数数量错误'
                    return False
                if(not self.__varPool.isVarExist(tempList[0])):
                    self._exp='变量不存在'
                
                varType=self.__varPool.getType(tempList[0])
                for now2 in range(1,tempList.__len__()):
                    if(self.__parameterofAssignCommandList[now1][now2]=='表达式'):
                        if(varType==0):
                            self.__expJudger=PicturesExpressionJudger.PicturesExpressionJudger()
                        elif(varType==1):
                            self.__expJudger=ArithmeticExpressionJudger.ArithmeticExpressionJudger()
                        elif(varType==2):
                            self.__expJudger=BooleanExpressionJudger.BooleanExpressionJudger()
                        elif(varType==3):
                            self.__expJudger=StringExpressionJudger.StringExpressionJudger()

                        if(not self.__expJudger.judge(tempList[now2])):
                            self._exp='表达式出现错误'
                            return False 

                return True            
            now1+=1
        return True



