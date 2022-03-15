import re
class Grammar:
    _instance=None
    
    def __new__(cls):
        
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
 

    __beginWordsList=[]
    __keyWordsList=[]
    __actionCommandList=[]
    __defineCommandList=[]
    __assignCommandList=[]
    __loopCommandList=[]
    __ifCommandList=[]  
    __commandList=[]
    Special__keyWordsList=[]
    SpecialKeyWordsMapping={}

    def __generateBeginWordsList(self):
        self.__beginWordsList=[]
        for line1 in self.__commandList:
            line1=line1.replace('$','')
            WordList=line1.split(' ')
            if(WordList[0]!='(.*?)' and WordList[0] not in self.__beginWordsList):
                self.__beginWordsList.append(WordList[0])
        

    def __generateKeyWordsList(self):
        self.__keyWordsList=self.OperatorList
        for line1 in self.__commandList:
            line1=line1.replace('$','')
            WordList=line1.split(' ')
            for line2 in WordList:
                if(line2!='(.*?)' and line2 not in self.__keyWordsList):
                    self.__keyWordsList.append(line2)
        
    

    def __generateCommandList(self,proList,list,parameterList):
        Now=0
        for line1 in proList:
            parameterList.append(re.findall(r'\((.*?)\)',line1))
            list.append(line1)
            for line2 in parameterList[Now]:
                list[Now]=list[Now].replace(line2,'.*?')
            Now=Now+1
      
     

    def __init__(self):
        pass


    def init(self):
        self.UnmappingOperatorKeywordList=['加','减','乘','除以']  
        self.UnmappingCmpoperKeywordList=['小于','大于','等于','小于等于','大于等于','不是','而且','或者']
        self.UnmappingPrioperKeywordList=['左括号','右括号']
        self.UnmappingPicoperatorKeywordList=['图存在于']
        self.UnmappingWordPicoperatorKeywordList=['文字存在于']

        #self.oper_list=self.operator_unmapping_keyword_list+self.cmpoper_unmapping_keyword_list+self.prioper_unmapping_keyword_list+self.picoperator_unmapping_keyword_list+self.word_picoperator_unmapping_keyword_list+self.special_keyword_list+self.cmpoper_keyword_list+self.operator_keyword_list+self.prioper_keyword_list+self.picoperator_keyword_list+self.word_picoperator_keyword_list
        
        self.OperatorKeywordList=['+','-','*','/']
        self.CmpoperKeywordList=['<','>','==','>=','<=','not','and','or']
        self.PrioperKeywordList=['(',')']
        self.PicoperatorKeywordList=['pic_in']
        self.WordPicoperatorKeywordList=['words_in']
        self.OperatorList=[]
        self.OperatorList+=self.UnmappingOperatorKeywordList
        self.OperatorList+=self.UnmappingCmpoperKeywordList
        self.OperatorList+=self.UnmappingPrioperKeywordList
        self.OperatorList+=self.UnmappingPicoperatorKeywordList
        self.OperatorList+=self.UnmappingWordPicoperatorKeywordList

        self.OperatorList+=self.OperatorKeywordList
        self.OperatorList+=self.CmpoperKeywordList
        self.OperatorList+=self.PrioperKeywordList
        self.OperatorList+=self.PicoperatorKeywordList
        self.OperatorList+=self.WordPicoperatorKeywordList

        self.__actionCommandList=[]
        self.__parameterofActionCommandList=[]
        self.__actionCommandListPro=[
        r'延迟 (算术表达式)$',
        r'鼠标 左移 (算术表达式)$',
        r'鼠标 右移 (算术表达式)$',
        r'鼠标 上移 (算术表达式)$',
        r'鼠标 下移 (算术表达式)$',
        r'鼠标 上滚轮 (算术表达式)$',
        r'鼠标 下滚轮 (算术表达式)$',      
        r'输出 (算术表达式)$',
        r'鼠标 左键 点击$',
        r'鼠标 中键 点击$',
        r'鼠标 右键 点击$',
        r'鼠标 左键 双击$',
        r'鼠标 中键 双击$',
        r'鼠标 右键 双击$',
        r'鼠标 左键 按下$',
        r'鼠标 中键 按下$',
        r'鼠标 右键 按下$',        
        r'鼠标 左键 松开$',
        r'鼠标 中键 松开$',
        r'鼠标 右键 松开$',
        r'鼠标 左键 拖动 起点 横坐标 (算术表达式) 纵坐标 (算术表达式) 终点 横坐标 (算术表达式) 纵坐标 (算术表达式)$',
        r'鼠标 右键 拖动 起点 横坐标 (算术表达式) 纵坐标 (算术表达式) 终点 横坐标 (算术表达式) 纵坐标 (算术表达式)$',
        r'鼠标 移动到 横坐标 (算术表达式) 纵坐标 (算术表达式)$',
        r'鼠标 移动到 画面 (图片表达式) 图中',
        r'鼠标 移动到 (图片表达式) 图的 (图片表达式) 图中',
        r'鼠标 移动到 画面 (字符串表达式) 文字中',
        r'鼠标 移动到 (图片表达式) 图的 (字符串表达式) 文字中',      
        r'打印 (字符串表达式)$',
        r'键盘 按下 (按键)键 持续 (算术表达式)$',
        r'键盘 按下 (按键)键$',
        r'键盘 松开 (按键)键$',
        r'连点器 (算术表达式) 次 横坐标 (算术表达式) 纵坐标 (算术表达式) 左键 间隔 (算术表达式)$',
        r'连点器 (算术表达式) 次 横坐标 (算术表达式) 纵坐标 (算术表达式) 右键 间隔 (算术表达式)$',
        r'等待图 (图片表达式) 出现$'
        ]
        self.__defineCommandList=[]
        self.__parameterofDefineCommandList=[]
        self.__defineCommandListPro=[
        r'定义 (变量类型) 变量 (变量名)$',
        r'定义 (变量类型) 变量 (变量名) 为 (表达式)$',
        r'定义 (变量类型) 变量 (变量名) = (表达式)$',
        ]
        self.__assignCommandList=[]
        self.__parameterofAssignCommandList=[]
        self.__assignCommandListPro=[
        r'令 (变量名) 为 (表达式)$',
        r'令 (变量名) = (表达式)$',
        ]
        self.__loopCommandList=[]
        self.__parameterofLoopCommandList=[]
        self.__loopCommandListPro=[
        r'循环开始$',
        r'直到 (布尔表达式)$',
        r'当 (布尔表达式)$',
        r'循环结束$',
        r'继续$',
        r'退出循环$',
        r'退出所有循环$',
        ]
        self.__loop1Mapping={
        '循环开始$':1,
        '直到 (.*?)$':-1
        }
        self.__loop2Mapping={
        '当 (.*?)$':1,
        '循环结束$':-1
        }
        self.__ifCommandList=[]
        self.__parameterofIfCommandList=[]
        self.__ifCommandListPro=[
        r'如果 (布尔表达式) 那么$',
        r'否则$',
        r'条件结束$',
        ]
        self.__ifMapping={
        '如果 (.*?) 那么$':1,
        '条件结束$':-1
        }
        self.__elseMapping={
        '否则$':1,
        }
        self.__booleanValueList=[
        'true',
        'false'
        ]
        self.__NoteChar='#'   #注释字符
        self.__generateCommandList(self.__actionCommandListPro,self.__actionCommandList,self.__parameterofActionCommandList)
        self.__generateCommandList(self.__defineCommandListPro,self.__defineCommandList,self.__parameterofDefineCommandList)
        self.__generateCommandList(self.__assignCommandListPro,self.__assignCommandList,self.__parameterofAssignCommandList)
        self.__generateCommandList(self.__loopCommandListPro,self.__loopCommandList,self.__parameterofLoopCommandList)
        self.__generateCommandList(self.__ifCommandListPro,self.__ifCommandList,self.__parameterofIfCommandList)
        self.__commandList=[]
        self.__commandList+=self.__actionCommandList
        self.__commandList+=self.__defineCommandList
        self.__commandList+=self.__assignCommandList
        self.__commandList+=self.__loopCommandList
        self.__commandList+=self.__ifCommandList
        self.__parameterofCommandList=[]
        self.__parameterofCommandList+=self.__parameterofActionCommandList
        self.__parameterofCommandList+=self.__parameterofDefineCommandList
        self.__parameterofCommandList+=self.__parameterofAssignCommandList
        self.__parameterofCommandList+=self.__parameterofLoopCommandList
        self.__parameterofCommandList+=self.__parameterofIfCommandList
        self.__generateBeginWordsList()
        self.__generateKeyWordsList()
        
    
        self.__equipmentList=[
        r'鼠标',
        r'键盘',
        r'定义',
        r'令',
        r'如果',
        r'那么',
        r'否则',
        r'条件结束',
        r'继续',
        r'退出循环',
        r'循环开始',
        r'直到',
        r'当',
        r'循环结束',
        r'退出所有循环',
        r'输出',
        r'打印',
        r'连点器',
        r'等待图'   
        ]
      
        self.__partList=[
        r'上滚轮',
        r'下滚轮',
        r'左键',
        r'右键',
        r'中键',
        r'松开 (.*?)键',
        r'按下 (.*?)键',
        r'令 (.*?) 为',
        r'令 (.*?) =',
        r' 变量 (.*?) 为',
        r' 变量 (.*?) =',
        r' 变量 (.*?)$'
        ]        

        self.__actionList=[
        r'延迟',
        r'左移',
        r'右移',
        r'上移',
        r'下移',
        r'点击',
        r'双击',
        r'松开',
        r'按下',
        r'按下',
        r'拖动',
        r'移动到',
        r'定义 (.*?) 变量',
        ]


 







    def getCommandList(self):
        return self.__commandList

    def getParameterofCommandList(self):
        return self.__parameterofCommandList

    def getOperatorList(self):
        return self.OperatorList

    def getBeginWordsList(self):
        return self.__beginWordsList
        
    def getActionCommandList(self):
        return self.__actionCommandList

    def getParameterofActionCommandList(self):
        return self.__parameterofActionCommandList

    def getDefineCommandList(self):
        return self.__defineCommandList
    
    def getParameterofDefineCommandList(self):
        return self.__parameterofDefineCommandList

    def getAssignCommandList(self):
        return self.__assignCommandList

    def getParameterofAssignCommandList(self):
        return self.__parameterofAssignCommandList

    def getLoopCommandList(self):
        return self.__loopCommandList

    def getParameterofLoopCommandList(self):
        return self.__parameterofLoopCommandList

    def getIfCommandList(self):
        return self.__ifCommandList

    def getParameterofIfCommandList(self):
        return self.__parameterofIfCommandList

    def getKeyWordsList(self):
        return self.__keyWordsList

    def getOperatorKeywordList(self):
        return self.OperatorKeywordList

    def getCmpoperKeywordList(self):
        return self.CmpoperKeywordList

    def getPrioperKeywordList(self):
        return self.PrioperKeywordList

    def getPrioperKeywordList(self):
        return self.PrioperKeywordList

    def getWordPicoperatorKeywordList(self):
        return self.WordPicoperatorKeywordList

    def getBooleanValueList(self):
        return self.__booleanValueList

    def loop1Mapping(self,command):
        if(not self.__loop1Mapping.__contains__(command)):
            return 0
        return self.__loop1Mapping[command]

    def loop2Mapping(self,command):
        if(not self.__loop2Mapping.__contains__(command)):
            return 0
        return self.__loop2Mapping[command]


    def ifMapping(self,command):
        if(not self.__ifMapping.__contains__(command)):
            return 0
        return self.__ifMapping[command]

    def elseMapping(self,command):
        if(not self.__elseMapping.__contains__(command)):
            return 0
        return self.__elseMapping[command]


    def getEquimentList(self):
        return self.__equipmentList

    def getPartList(self):
        return self.__partList

    def getActionList(self):
        return self.__actionList

    def getNoteChar(self):
        return self.__NoteChar