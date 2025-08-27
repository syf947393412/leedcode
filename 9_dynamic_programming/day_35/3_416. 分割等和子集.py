from typing import List


class Solution:
    def canPartition(self, nums: List[int]) :
        nums_sum=sum(nums)
        # 关键优化：如果总和是奇数，直接返回False
        if nums_sum % 2 == 1:
            return False
        target=nums_sum//2
        dp=[0]*(target+1)

        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        # 如果dp[target]等于target，说明可以选出和为target的子集

        return dp[target] == target

nums=[1,2,3,5]
so=Solution()
print(so.canPartition(nums))


