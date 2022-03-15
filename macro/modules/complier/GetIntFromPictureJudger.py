import re
from macro.modules.complier import ArithmeticExpressionJudger

class GetIntFromPictureJudger:
    def __init__(self,int_var_list):
        self.IntFromPic=r'画面 左上角 横坐标 (.*?) 纵坐标 (.*?) 右下角 横坐标 (.*?) 纵坐标 (.*?) 的数字$'
        self.ExpJudger=ArithmeticExpressionJudger.ArithmeticExpressionJudger(int_var_list)

    def formatJudge(self,str):
        if(re.findall(self.IntFromPic,str)):
            return True
        else:
            return False

    def judge(self,str):
        if(not self.formatJudge(str)):
            return False 
        temp=re.findall(self.IntFromPic,str)
        print(temp)
        for i in range(0,4):
            if(not self.ExpJudger.judge(temp[0][i])):
                return False
        return True 