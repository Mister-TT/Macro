

import sys
sys.path.append("")
from macro.modules.complier.expressionjudger import ExpressionJudgerStrategy
from macro.modules.complier.pool import KeyPool

class KeyExpressionJudger(ExpressionJudgerStrategy.ExpressionJudgerStrategy):
    def __init__(self):
        ExpressionJudgerStrategy.ExpressionJudgerStrategy.__init__(self)
        self.__keyPool=KeyPool.KeyPool()
    
    def judge(self,str):
        return self.__keyPool.judge(str)