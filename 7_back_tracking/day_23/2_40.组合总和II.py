from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        used=[False]*len(candidates)   #！
        self.backtracing(candidates,target,0,[],result,0,used)
        return result

    def backtracing(self,candidates,target,sum,path,result,start_index,used):
        if sum>target:
            return
        if sum==target:
            result.append(path[:])

        for i in range(start_index,len(candidates)):
            #!去重操作
            if i>0 and candidates[i]==candidates[i-1] and used[i-1]==False:
                #used[i-1]是False  used[i]是True 说明是树层的重复
                continue
            path.append(candidates[i])
            used[i]=True  #!
            sum+=candidates[i]
            self.backtracing(candidates, target, sum, path, result, i+1,used)
            path.pop()
            used[i] =False  #!
            sum-=candidates[i]
        return
