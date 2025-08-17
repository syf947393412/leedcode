from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        used=[0]*len(nums)
        nums.sort()
        self.backtracing(nums,result,[],0,used)
        return result

    def backtracing(self,nums,result,path,start_index,used):
        result.append(path[:])
        if start_index==len(nums):
            return

        for i in range(start_index,len(nums)):
            # if i>0 and nums[i]==nums[i-1]:  #!也有可能是树枝之间的重复
            if i > 0 and nums[i] == nums[i - 1] and used[i-1]==0:
                continue
            path.append(nums[i])
            used[i]=1   #!
            self.backtracing(nums,result,path,i+1,used)
            used[i]=0
            path.pop()
        return