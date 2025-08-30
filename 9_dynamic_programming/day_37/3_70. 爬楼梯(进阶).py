from typing import List


def combinationSum4( m, n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1

    for j in range(n + 1):
        for i in range(1,m+1):
            if j >= i:
                dp[j] += dp[j - i]
    return dp[n]
m = 2
n = 3
print(combinationSum4(m,n=3))