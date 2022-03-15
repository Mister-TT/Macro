
from macro.modules.complier import Grammar
from macro.modules.complier.pool import KeyPool
from macro.modules.complier import OperatorConverter
import re
class CommandHandler:

    def __init__(self):
        self.__grammar=Grammar.Grammar()
        self.__keyPool=KeyPool.KeyPool()
        self.__converter=OperatorConverter.OperatorConverter()        
        self.__equipmentList=self.__grammar.getEquimentList()
        self.__partList=self.__grammar.getPartList()
        self.__actionList=self.__grammar.getActionList()
        self.__commandList=self.__grammar.getCommandList()
        self.__parameterofCommandList=self.__grammar.getParameterofCommandList()

    def getEquipment(self,command):
        for line in self.__equipmentList:
            if(line in command):
                return line
        return ''
    def getPart(self,command):
        for line in self.__partList:
            if(line in command):
                return line
            if(re.search(line,command)):
                return self.__keyPool.convert(re.findall(line,command)[0])
        return ''

    def getAction(self,command):
        for line in self.__actionList:
            if(line in command):
                return line
            if(re.search(line,command)):
                return re.findall(line,command)[0]
        return ''

    def transferExp(self,exp):
        parameters_list=[]
        unit=exp.split(' ')
        for line in unit:
            line=self.__converter.Convert(line)
            parameters_list.append(line)
            
        return parameters_list

    def ParametersBegin(self,command):#历史遗留问题
        parametersList=[]
        if(re.match(r'鼠标 移动到 横坐标 (.*?) 纵坐标 (.*?)$',command)):
            parametersList.append('坐标')
        if(re.match(r'鼠标 移动到 画面 (.*?) 图中$',command)):
            parametersList.append('小图截屏')
        if(re.match(r'鼠标 移动到 (.*?) 图的 (.*?) 图中$',command)):
            parametersList.append("小图大图")
        if(re.match(r'鼠标 移动到 画面 (.*?) 文字中$',command)):
            parametersList.append('文字截屏')
        if(re.match(r'鼠标 移动到 (.*?) 图的 (.*?) 文字中$',command)):
            parametersList.append('文字大图')
 
        return parametersList

    def getParameters(self,command):
        parametersList=self.ParametersBegin(command)
        for now1 in range(0,self.__commandList.__len__()):
            if(self.__parameterofCommandList[now1]==[]):
                continue
            if(re.match(self.__commandList[now1],command)):
                tempList=[]
                temp=[]
                temp=(re.findall(self.__commandList[now1],command))
                
                if(isinstance(temp[0],str)):
                    tempList=temp
                else:
                    for line in temp[0]:
                        tempList.append(line)
                for now2 in range(0,self.__parameterofCommandList[now1].__len__()):
                    if('表达式' in self.__parameterofCommandList[now1][now2]):
                        parametersList+=self.transferExp(tempList[now2])
        if(parametersList==[]):
            parametersList=['0']           
        return parametersList








                     