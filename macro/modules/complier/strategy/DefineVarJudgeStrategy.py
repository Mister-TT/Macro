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


class DefineVarJudgeStrategy(JudgeStrategy.JudgeStrategy):
    _instance=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance 
        
    def __init__(self):
        JudgeStrategy.JudgeStrategy.__init__(self)
        self.__defineCommandList=self._grammar.getDefineCommandList()
        self.__parameterofDefineCommandList=self._grammar.getParameterofDefineCommandList()
        self.__expJudger=ExpressionJudgerStrategy.ExpressionJudgerStrategy()       
        self.__varPool=VarPool.VarPool()
    def judge(self,command):
        now1=0
        
        for line1 in self.__defineCommandList:
            if(self.__parameterofDefineCommandList[now1].__len__()==0):
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
                if(tempList.__len__()!=self.__parameterofDefineCommandList[now1].__len__()):
                    self._exp='参数数量错误'
                    return False

                varType=self.__varPool.getVarType(tempList[0])
                if(self.__varPool.isVarExist(tempList[1])):
                    self._exp='变量名字和已有变量重复'
                    return False

                if(tempList[1] in self._grammar.getKeyWordsList()):
                    self._exp='变量名字和已有关键词重复'
                    return False   

                self.__varPool.pushVar(varType,tempList[1])
                
                for now2 in range(2,tempList.__len__()):
                    if(self.__parameterofDefineCommandList[now1][now2]=='表达式'):
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



