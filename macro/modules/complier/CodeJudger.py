import re
import sys
sys.path.append("")
from macro.modules.complier.strategy import JudgeStrategy
from macro.modules.complier.strategy import ActionJudgeStrategy
from macro.modules.complier.strategy import DefineVarJudgeStrategy
from macro.modules.complier.strategy import AssignmentJudgeStrategy
from macro.modules.complier.strategy import LoopJudgeStrategy
from macro.modules.complier.strategy import IfJudgeStrategy
from macro.modules.complier.pool import VarPool
from macro.modules.complier import Grammar
class CodeJudger:
    def __init__(self):
        self.NoteChar='#'
        self.__judger=JudgeStrategy.JudgeStrategy()
        self.varPool=VarPool.VarPool()
        self.varPool.init()
        self.__errorList=[]
        self.__errorMess=''
        self.__grammar=Grammar.Grammar()
        self.__actionCommandList=self.__grammar.getActionCommandList()
        self.__defineCommandList=self.__grammar.getDefineCommandList()
        self.__assignCommandList=self.__grammar.getAssignCommandList()
        self.__loopCommandList=self.__grammar.getLoopCommandList()
        self.__ifCommandList=self.__grammar.getIfCommandList()

    def __read(self,FilePath):
        self.UserCommandList=open(FilePath, 'r', encoding='utf8').readlines()
        i=0
        print(self.UserCommandList)
        for line1 in self.UserCommandList:
            line1=line1.replace('\n','')
            if(line1.find(self.NoteChar)>=0):
                temp=line1.find(self.NoteChar)
                line1=line1[:temp]
            line1=line1.strip(' ')
            self.UserCommandList[i]=line1
            i+=1
        # self.__judger=ActionJudgeStrategy.ActionJudgeStrategy()
        # for line in self.UserCommandList:
        #     if(self.__judger.judge(line)):
        #         print(111)
        print(self.UserCommandList)


    def __chooseStrategy(self,command):
        for line in self.__actionCommandList:
            if(re.match(line,command)):
                return ActionJudgeStrategy.ActionJudgeStrategy()

        for line in self.__defineCommandList:
            if(re.match(line,command)):
                return DefineVarJudgeStrategy.DefineVarJudgeStrategy()

        for line in self.__assignCommandList:
            if(re.match(line,command)):
                return AssignmentJudgeStrategy.AssignmentJudgeStrategy()

        for line in self.__loopCommandList:
            if(re.match(line,command)):
                return LoopJudgeStrategy.LoopJudgeStrategy()

        for line in self.__ifCommandList:
            if(re.match(line,command)):
                return IfJudgeStrategy.IfJudgeStrategy()

        return None

    def getErrorList(self):
        return self.__errorList

    def judgeFile(self,FilePath):
        self.__errorList = []
        self.__read(FilePath)
        self.varPool.init()
        now=1
        for line in self.UserCommandList:
            if(line==''):
                continue
            self.__errorMess=''
            self.__judger=self.__chooseStrategy(line)
            if(self.__judger==None):
                self.__errorMess='无法识别的命令'
            else:    
                if(not self.__judger.judge(line)):
                    self.__errorMess=self.__judger.getExp()
            if(self.__errorMess!=''):
                self.__errorList.append('第'+str(now)+'行，'+self.__errorMess+'，其内容为：'+line)
            now+=1

        self.__judger=LoopJudgeStrategy.LoopJudgeStrategy()
        if(not self.__judger.isLoopFinished()):
            self.__errorList.append('循环没结束')
        self.__judger.reset()

        self.__judger=IfJudgeStrategy.IfJudgeStrategy()
        if(not self.__judger.isIfFinished()):
            self.__errorList.append('条件没结束')
        self.__judger.reset()
        
        if(self.__errorList!=[]):
            return False
        else:
            return True

