from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        self.backtracing(s,[],result,0)
        return result

    def is_palidrome(self,s:str):
        left=0
        right=len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

    def backtracing(self,s,path,result,start_index):
        if start_index==len(s):
            result.append(path[:])
            return

        for i in range(start_index,len(s)):
            if not self.is_palidrome((s[start_index:i+1])):
                continue
            path.append(s[start_index:i+1])
            self.backtracing(s,path,result,i+1)
            path.pop()

        return