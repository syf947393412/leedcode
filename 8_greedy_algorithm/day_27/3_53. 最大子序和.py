from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max_sum=-float("inf")   #!
        for i in range(len(nums)):
            sum=sum+nums[i]
            if sum<0:
                sum=0
            if sum>max_sum:
                max_sum=sum
        return max_sum

