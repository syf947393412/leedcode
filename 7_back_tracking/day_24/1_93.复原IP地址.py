from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result=[]
        self.backtracing(s,0,0,result,"")
        return result

    def backtracing(self,s:str,pointNum,start_index,result,current):
        if pointNum==3:
            if self.is_valid(s,start_index,len(s)-1):
                # valid_ip=current+s[start_index:len(s)]
                valid_ip=current+s[start_index:]

                result.append(valid_ip)
                return

        for i in range(start_index,len(s)):
            if self.is_valid(s,start_index,i):
                pointNum+=1

                # self.backtracing(s,pointNum,start_index+1,result,current+s[start_index:i+1]+".")
                #current+s[start_index:i+1]+"."
                #start_index:i+1
                self.backtracing(s,pointNum,i+1,result,current+s[start_index:i+1]+".")

                pointNum-=1
        return

    def is_valid(self,s,start,end):
        if start>end:
            return False
        if s[start]=="0" and start!=end:   #!
            return False
        num=int(s[start:end+1])
        # if num>255 and num<0:
        if num>255 or num<0:
            return False
        else:
            return True