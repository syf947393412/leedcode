from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=[0]*len(nums)
        self.backtracing(nums,result,[],used)
        return result

    def backtracing(self,nums,result,path,used):
        if len(path)==len(nums):
            result.append(path[:])

        for i in range(len(nums)):
            if used[i]==1:
                continue
            used[i]=1
            path.append(nums[i])
            self.backtracing(nums,result,path,used)
            used[i]=0
            path.pop()

        return