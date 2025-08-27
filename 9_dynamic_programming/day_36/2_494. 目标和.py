from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum=sum(nums)
        if (nums_sum+target)%2==1:
            return 0
        bagSize =(nums_sum+target)//2

        dp=[[0]*(bagSize+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=1
        dp[0][1]=1

        for i in range(1,len(nums)):
            for j in range(bagSize+1):
                if j>=nums[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[len(nums)-1][bagSize]




so=Solution()
nums = [1,1,1,1,1]
target = 3
print(so.findTargetSumWays(nums,target))



