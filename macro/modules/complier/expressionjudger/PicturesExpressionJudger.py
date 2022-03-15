import re
import sys
sys.path.append("")
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier import OperatorConverter
from macro.modules.complier import Grammar
from macro.modules.complier.pool import VarPool

class PicturesExpressionJudger(ExpressionJudgerStrategy.ExpressionJudgerStrategy):
    def __init__(self):
        ExpressionJudgerStrategy.ExpressionJudgerStrategy.__init__(self)
        self.Grammar=Grammar.Grammar()
        self.__varPool=VarPool.VarPool()
        self.Converter=OperatorConverter.OperatorConverter()
             

    def judge(self,str):   
        PicVarList=self.__varPool.getVarList(self.__varPool.getVarType('图片'))
        return str in PicVarList
