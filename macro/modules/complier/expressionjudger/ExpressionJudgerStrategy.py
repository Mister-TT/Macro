import re
import sys
sys.path.append("")
from macro.modules.complier import Grammar
from macro.modules.complier.pool import VarPool

class ExpressionJudgerStrategy:
    def __init__(self):
        self._grammar=Grammar.Grammar()
        self._varPool=VarPool.VarPool()

    def judge(self,str):
        return True