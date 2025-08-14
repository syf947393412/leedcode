from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.backtracing(candidates,[],target,result,0)
        return result

    def backtracing(self,candidates,path,target,result,start_index):
        if sum(path)>target:
            return
        if sum(path)==target:
            result.append(path[:])
            return

        for i in range(start_index,len(candidates)):
            path.append(candidates[i])
            self.backtracing(candidates,path,target,result,i)    #!i-->start_index：含去重，但又可以重复
            path.pop()
        return