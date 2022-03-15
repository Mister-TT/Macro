import re
import sys
sys.path.append("")
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier import OperatorConverter
from macro.modules.complier import Grammar
from macro.modules.complier.pool import VarPool

class ArithmeticExpressionJudger(ExpressionJudgerStrategy.ExpressionJudgerStrategy):
    def __init__(self):
        ExpressionJudgerStrategy.ExpressionJudgerStrategy.__init__(self)
        self.Grammar=Grammar.Grammar()
        self.OperatorKeywordList=self.Grammar.getOperatorKeywordList()
        self.CmpoperKeywordList=self.Grammar.getCmpoperKeywordList()
        self.PrioperKeywordList=self.Grammar.getPrioperKeywordList()
        self.PicoperatorKeywordList=self.Grammar.getPrioperKeywordList()
        self.WordPicoperatorKeywordList=self.Grammar.getWordPicoperatorKeywordList()
        self.__varPool=VarPool.VarPool()
        

        self.prioper_count={
        '左括号':1,
        '右括号':-1,
        '(':1,
        ')':-1
        }

        self.Converter=OperatorConverter.OperatorConverter()
             

    def judge(self,str):   
        IntList=self.__varPool.getVarList(self.__varPool.getVarType('整型'))
        unit=str.split(' ')
        #print(unit)
        isoper=False
        cnt=0
        for i in range (0,len(unit)):
            unit[i]=self.Converter.Convert(unit[i])
            if(isoper):
                if(unit[i] not in self.OperatorKeywordList):
                    if(unit[i] == self.PrioperKeywordList[0]):
                        self.exp='表达式的括号存在错误'
                        return False 
                    if(unit[i]==self.PrioperKeywordList[1]):
                        cnt+=self.prioper_count[unit[i]]
                        if(cnt<0):
                            self.exp='表达式的括号存在错误'
                            return False      
                        isoper=not isoper  
                    else:                      
                        self.exp='表达式运算符错误'
                        return False  
                         
            else:
                if(unit[i] == self.PrioperKeywordList[1]):
                    self.exp='表达式的括号存在错误'
                    return False  
                if(unit[i] == self.PrioperKeywordList[0]):
                    cnt+=self.prioper_count[unit[i]]
                    if(cnt<0):
                        self.exp='表达式的括号存在错误'
                        return False      
                    isoper=not isoper
                else:
                    if(unit[i] not in IntList and(not unit[i].isdigit())):
                        self.exp='表达式变量错误'
                        return False                     
            isoper=not isoper


        if(not isoper):
            self.exp='表达式错误'
            return False
        if(cnt!=0):
            self.exp='表达式的括号存在错误'
            return False        

        return True

