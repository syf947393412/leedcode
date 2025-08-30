from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0]=1
        # 处理第一种硬币
        for j in range(1, amount + 1):
            if j % coins[0] == 0:  # 只有能整除时才有方法
                dp[0][j] = 1


        # for i in range(len(coins)):
        for i in range(1,len(coins)):
            # for j in range(amount):
            for j in range(amount+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j]+dp[i][j-coins[i]]

        return dp[len(coins)-1][amount]