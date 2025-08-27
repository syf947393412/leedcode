from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        used=[0]*len(nums)
        result=[]
        self.backtracing(nums,result,[],0,used)

        return result

    def backtracing(self,nums,result,path,start_index,used):
        if len(path)>=2:
            result.append(path[:])


        for i in range(start_index,len(nums)):
            if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
                continue
            if i>0 and nums[i]<path[-1]:
                continue

            path.append(nums[i])
            used[i]=1
            self.backtracing(nums,result,path,i+1,used)
            used[i]=0
            path.pop()

        return

# nums =[4,6,7,7]
nums = [4,4,3,2,5]
so=Solution()
print(so.findSubsequences(nums))

