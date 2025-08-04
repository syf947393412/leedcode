from typing import List
from operator import add,sub,mul


class Solution:
    def div(self,num1:int,num2:int):
        result=0
        if num1*num2>0:
            result=int(num1/num2)  #!
        elif num1*num2<0:
            # result=-abs(num1)//abs(num2)  #!
            result = -(abs(num1) // abs(num2))
        return result
    def evalRPN(self, tokens: List[str]) -> int:
        op_map={"+":add,"-":sub,"*":mul,"/":self.div}   #!
        stack=[]
        for item in tokens:
            if item not in ["+","-","*","/"]:
                stack.append(int(item))
            else:
                num2=stack.pop()
                num1=stack.pop()
                temp_result=op_map[item](num1,num2)
                stack.append(temp_result)
        return stack.pop()
