


class VarPool:
    _instance=None
    
    def __new__(cls):
        
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass


    def init(self):
        self.__varNum=4
        self.__varTypeList=[
        '图片',
        '整型',
        '字符串',
        '布尔型'            
        ]
        self.__varPool=[]
        for i in range (self.__varNum):
            self.__varPool.append([])   
        self.__mapping={
        '图片': 0,
        '整型': 1,
        '字符串': 2,
        '布尔型': 3            
        }    

    def getVarType(self,varType):
        if(not self.__mapping.__contains__(varType)):
            return -1
        
        return self.__mapping[varType]

    def isVarExist(self,varName):
        for line in self.__varPool:
            if(varName in line):
                return True
        return False

    def pushVar(self,varType,varName):
        self.__varPool[varType].append(varName)
        
    def popVar(self,varType):
        self.__varPool[varType].pop()

    def getVarList(self,varType):
        return self.__varPool[varType] 

    def getType(self,varName):
        if(not self.isVarExist(varName)):
            return -1
        for i in range(0,self.__varNum):
            if(varName in self.__varPool[i]):
                return i    