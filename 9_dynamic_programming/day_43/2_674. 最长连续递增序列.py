from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)

        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                dp[i]=dp[i-1]+1

        return max(dp)

nums = [1,3,5,4,7]
so=Solution()
print(so.findLengthOfLCIS(nums))