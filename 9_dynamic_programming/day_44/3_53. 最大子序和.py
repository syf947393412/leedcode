from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp2=[0]*len(nums)   #
        #！
        dp[0]=nums[0]
        dp2[0]=nums[0]   #

        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            dp2[i]=max(dp[i-1]+nums[i],dp[i-1])   #
        print("dp是：")
        print(dp)
        print("dp2是：")
        print(dp2)
        return max(dp)   #

nums=[-2,1,-3,4,-1,2,1,-5,4]
so=Solution()
print(so.maxSubArray(nums))