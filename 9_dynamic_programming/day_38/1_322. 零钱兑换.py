from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[0]*(amount+1)
        for i in range(1,amount+1):
            dp[i]=float("inf")

        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])
        if dp[amount]==float("inf"):
            return -1
        return dp[amount]