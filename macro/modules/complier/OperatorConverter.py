

class OperatorConverter:
    def __init__(self):
        self.Mapping={
        '加':'+',
        '减':'-',
        '乘':'*',
        '除以':'/',
        '小于':'<',
        '大于':'>',
        '等于':'==',
        '小于等于':'<=',
        '大于等于':'>=',
        '而且':'and',
        '不是':'not',
        '或者':'or',         
        '真':'true',
        '非':'false',
        '左括号':'(',
        '右括号':')',
        '(':'(',
        ')':')'
        }



    def Convert(self,str):
        if(self.Mapping.__contains__(str)):
            return self.Mapping[str]
        else:
            return str