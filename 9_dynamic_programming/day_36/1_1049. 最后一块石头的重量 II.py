from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        sum_stone=sum(stones)
        target=sum_stone//2
        dp = [0] * (target+1) #!

        for i in range(len(stones)):
            # for j in range(target+1,-1,-1):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return sum_stone-dp[target]-dp[target]

stones = [2,7,4,1,8,1]
so=Solution()
print(so.lastStoneWeightII(stones))