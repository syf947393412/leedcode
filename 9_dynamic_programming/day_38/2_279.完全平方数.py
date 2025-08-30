from typing import List
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float("inf")]*(n+1)

        dp[0]=0

        for i in range(1,n+1):
            for j in range(i**2,n+1):  #!
                dp[j] = min(dp[j -i**2] + 1, dp[j])  #!
        if dp[n]==float("inf"):
            return -1

        return dp[n]