import sys
sys.path.append("")
from macro.modules.complier import Excuter
from macro.modules.complier import Grammar


class CodeExcuter:
    def __init__(self):
        self.__excuter=Excuter.Excuter()
        self.__grammar=Grammar.Grammar()
        self.__userCommandList=[]
    def __read(self,FilePath):
        self.__userCommandList=open(FilePath, 'r', encoding='utf8').readlines()
        i=0
        print(self.__userCommandList)
        for line1 in self.__userCommandList:
            line1=line1.replace('\n','')
            if(line1.find(self.__grammar.getNoteChar())>=0):
                temp=line1.find(self.__grammar.getNoteChar())
                line1=line1[:temp]
            line1=line1.strip(' ')
            self.__userCommandList[i]=line1
            i+=1
        # self.__judger=ActionJudgeStrategy.ActionJudgeStrategy()
        # for line in self.__userCommandList:
        #     if(self.__judger.judge(line)):
        #         print(111)
        print(self.__userCommandList)

    def excuteFile(self,filePath,thd=None):
        self.__read(filePath)
        self.__excuter.excute(self.__userCommandList,thd)

