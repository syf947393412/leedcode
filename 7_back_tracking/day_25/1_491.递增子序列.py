from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        # nums.sort()
        used=[0]*len(nums)
        self.backtracing(nums,result,[],0,used)

        return result

    def backtracing(self,nums,result,path,start_index):
        # if len(path)==2:
        if len(path)>=2:
            # result.append(path)
            result.append(path[:])
        if start_index==len(nums):
            return

        uset=set()  #!去重
        for i in range(start_index,len(nums)):
            #！去重逻辑：①用or   ②nums[i] in uset
            # if i>0 and nums[i]<=nums[i-1] and used[i-1]==0:
            if (i>0 and nums[i]<path[-1]) or nums[i] in uset :
                continue

            path.append(nums[i])
            # used[i]=1   #!
            uset.add(nums[i])  #!set插入用add

            #回溯时，不加uset
            # self.backtracing(nums,result,path,i+1,used)
            self.backtracing(nums,result,path,i+1)

            path.pop()
        return

