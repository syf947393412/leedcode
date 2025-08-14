from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.path=[]
        self.result=[]
        def backtracking(n,k,start_index):
            if len(self.path)==k:
                # self.result.append(self.path)   #！
                self.result.append(self.path[:])
                return     #!找到组合后立即返回，避免继续执行

            # for i in range(start_index,n):
            for i in range(start_index,n+1):   #——>1,2,3,4:
                self.path.append(i)
                # backtracking(n,k,start_index+1)   #!
                backtracking(n,k,i+1)

                self.path.pop()
        backtracking(n,k,1)
        return self.result

