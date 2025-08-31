from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        result1=self.robRange(nums,0,len(nums) - 2)
        result2=self.robRange(nums,1,len(nums)-1)
        return max(result1,result2)

    def robRange(self, nums, start, end):
        if end == start:
            return nums[start]

        # dp数组的长度
        length = end - start + 1
        dp = [0] * length

        # 使用相对索引访问dp数组
        dp[0] = nums[start]
        dp[1] = max(nums[start], nums[start + 1])

        # 循环也应该使用相对索引
        for i in range(2, length):  # i是相对索引
            # dp[i]对应原始索引start+i的位置
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[start + i])

        return dp[length - 1]
