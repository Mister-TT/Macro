import sys
sys.path.append("")
from macro.modules.complier import CommandHandler

class Transfer:

    def __init__(self):
        self.__handler=CommandHandler.CommandHandler()
        self.__equipment=[]
        self.__part=[]
        self.__action=[]
        self.__parameters=[]
    

    def __clear(self):
        self.__equipment=[]
        self.__part=[]
        self.__action=[]
        self.__parameters=[]
    
    def transfer(self,userCommandList):
        self.__clear()
        self.__top=0
        for line in userCommandList:
            print(line)
            self.__parameters.append([])
            self.__equipment.append(self.__handler.getEquipment(line))
            self.__part.append(self.__handler.getPart(line))
            self.__action.append(self.__handler.getAction(line))
            self.__parameters[self.__top]=(self.__handler.getParameters(line))
            
            self.__top+=1





        print(self.__equipment)#变量类型
        print(self.__part)#变量名字
        print(self.__action)#定义
        print(self.__parameters)
    
        #self.equipment[]
        #self.part[]
        #self.action[]
        #self.parameters1[]
        #self.parameters2[]

    def getTop(self):
        return self.__top

    def getEquipment(self):
        return self.__equipment

    def getPart(self):
        return self.__part

    def getAction(self):
        return self.__action

    def getParamters(self):
        return self.__parameters