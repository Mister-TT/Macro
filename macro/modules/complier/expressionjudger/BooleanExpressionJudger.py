import re
import sys
sys.path.append("")
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier import OperatorConverter
from macro.modules.complier import Grammar
from macro.modules.complier.pool import VarPool

class BooleanExpressionJudger(ExpressionJudgerStrategy.ExpressionJudgerStrategy):
    def __init__(self):
        ExpressionJudgerStrategy.ExpressionJudgerStrategy.__init__(self)
        self.Grammar=Grammar.Grammar()
        self.OperatorKeywordList=self.Grammar.getOperatorKeywordList()
        self.CmpoperKeywordList=self.Grammar.getCmpoperKeywordList()
        self.PrioperKeywordList=self.Grammar.getPrioperKeywordList()
        self.PicoperatorKeywordList=self.Grammar.getPrioperKeywordList()
        self.WordPicoperatorKeywordList=self.Grammar.getWordPicoperatorKeywordList()
        self.__booleanValueList=self.Grammar.getBooleanValueList()
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
        PicVarList=self.__varPool.getVarList(self.__varPool.getVarType('整型'))
        BooleanVarList=self.__varPool.getVarList(self.__varPool.getVarType('整型'))
        unit=str.split(' ')
        isoper=False
        cnt=0
        is_pic_pic=False
        is_words_pic=False
        #print(unit)
        for i in range (0,len(unit)):
            unit[i]=self.Converter.Convert(unit[i])
            if(isoper):
                if((unit[i] not in self.OperatorKeywordList) and(unit[i] not in self.CmpoperKeywordList)):
                    if(unit[i] == self.PrioperKeywordList[0]):
                        self.exp='表达式的括号存在错误'
                        return False 

                    if(unit[i] in self.PicoperatorKeywordList):
                        is_pic_pic=True
                    
                    if(unit[i] in self.WordPicoperatorKeywordList):
                        is_words_pic=True

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
                    if((unit[i]!='画面')and(unit[i] not in IntList)and(unit[i] not in PicVarList)and (unit[i] not in BooleanVarList) and(not unit[i].isdigit())and(unit[i] not in self.__booleanValueList)):
                        if(is_pic_pic):
                            is_pic_pic=False
                            if((unit[i] not in PicVarList and unit[i]!='画面') or unit[i-2] not in PicVarList):
                                self.exp='图片变量错误'
                                return False
                        if(is_words_pic):
                            is_words_pic=False
                            if(unit[i] not in PicVarList and unit[i]!='画面'):
                                self.exp='图片变量错误'
                                return False
                        if(unit[i]=='不是'):
                            isoper=not isoper
                        else:
                            if(i+1<len(unit) and (unit[i+1] in self.WordPicoperatorKeywordList)):
                                hehe=1
                            else:
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
