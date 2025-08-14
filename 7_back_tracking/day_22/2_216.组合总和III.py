from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.backtracing(k,n,1,sum=0,path=[],result=result)
        return result

    def backtracing(self,k,n,start_index,sum=0,path=[],result=[],):
        if sum==n and len(path)==k:
            result.append(path[:])
            return

        for i in range(start_index,n+1):
            path.append(i)
            sum=sum+i
            self.backtracing(k,n,i+1,sum,path,result)
            sum-=i
            path.pop()
        return