
import re
from macro.modules.complier import Grammar
class CodeModifier:


    def __init__(self):

        self.Grammar=Grammar.Grammar()
        self.BeginWordsList=self.Grammar.getBeginWordsList()
        self.KeyWordsList=self.Grammar.getKeyWordsList()
        self.SpecialKeyWordsList=['>=','<=','==','小于等于','大于等于']

        self.SpecialKeyWordsMapping={
        '小于等于':'小于  等于',
        '<=':'<  =',
        '大于等于':'大于  等于',
        '>=':'>  =',
        '==':'=  ='
        }
        self.__userCommandList=[]


    def __modify(self,FilePath):
        self.__userCommandList=open(FilePath, 'r', encoding='utf8').read()
        self.space=[]
        self.__userCommandList=self.__userCommandList.replace('，','')
        self.__userCommandList=self.__userCommandList.replace('\n','')
        self.__userCommandList=self.__userCommandList.strip(' ')
        for line in self.BeginWordsList:

            self.__userCommandList=self.__userCommandList.replace(line,'\n'+line)

        self.__userCommandList=self.__userCommandList.strip('\n')    
        self.__userCommandList=self.__userCommandList.split('\n')
        i=0
        for line1 in self.__userCommandList:
            for line2 in self.KeyWordsList:
                line1=line1.replace(line2,' '+line2+' ')

            for line2 in self.SpecialKeyWordsList:
                line1=line1.replace(self.SpecialKeyWordsMapping[line2],line2)

            line2=line2.replace('= =','==')
            if(line1.find('字符串')>0 and line1.find('为')>0):
                temp=line1.find('为')
                stemp=line1[temp+2:]
                line1=line1[:temp+2]+stemp.replace(' ','')

            if(line1.find('字符串')>0 and line1.find('=')>0):
                temp=line1.find('=')
                stemp=line1[temp+2:]
                line1=line1[:temp+2]+stemp.replace(' ','')

            while(line1!=line1.replace('  ',' ')):
                line1=line1.replace('  ',' ')
            line1=line1.strip(' ')
            
            self.__userCommandList[i]=line1
            i+=1
        #print(self.user_command_list)
        i=0
        cnt=0
        for line1 in self.__userCommandList:
            self.space.append(cnt)
            temp=line1.split(' ')

            if(len(temp)!=0):
                if(temp[0]=='如果' or temp[0]=='循环开始' or temp[0]=='当'):
                    cnt+=1
                if(temp[0]=='那么' or temp[0]=='否则'):
                    self.space[i]-=1
                if(temp[0]=='条件结束'or temp[0]=='直到' or temp[0]=='循环结束'):
                    cnt-=1
                    self.space[i]=cnt
          
            i+=1
        return

      
    def modifyFile(self,FilePath):
        self.__modify(FilePath)
        i = 0
        f = open(FilePath, 'w', encoding='utf-8')
        for line1 in self.__userCommandList:
            print(self.space[i]*'    '+line1,file=f)
            print(self.space[i]*'    '+line1)
            i+=1
        f.close()
        return True