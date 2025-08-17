from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backtracing(nums,result,[],0)
        return result

    def backtracing(self,nums,result,path,start_index):
        #! path.append(nums[start_index])
        result.append(path[:])
        if start_index==len(nums):
            return

        for i in range(start_index,len(nums)):
            path.append(nums[i])
            self.backtracing(nums,result,path,i+1)
            path.pop()
        return
