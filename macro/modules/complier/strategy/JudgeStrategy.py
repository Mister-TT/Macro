


from macro.modules.complier import Grammar



class JudgeStrategy:

    def __init__(self):
        self._grammar=Grammar.Grammar()
        self._exp=''

    def judge(self,str):
        return True

    def getExp(self):
        return self._exp


