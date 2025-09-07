from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) :


        dp=[1]*len(nums)
        dp[0]=1
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[j]+1,dp[i])

        # return max(dp)
        return dp

nums=[0,1,0,3,2,3]
so=Solution()
print(so.lengthOfLIS(nums))