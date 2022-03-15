
import re
import sys
sys.path.append("")
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier import OperatorConverter
from macro.modules.complier import Grammar
from macro.modules.complier.pool import VarPool

class StringExpressionJudger(ExpressionJudgerStrategy.ExpressionJudgerStrategy):
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
        return True
