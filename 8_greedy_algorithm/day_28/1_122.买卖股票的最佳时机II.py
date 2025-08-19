from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i in range(len(prices)-1):
            result+=max(0,prices[i+1]-prices[i])
        return result