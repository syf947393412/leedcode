class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)]for _ in range(m)]
        for i in range(n):
            dp[0][i]=1
        for j in range(m):
            dp[j][0]=1

        for i in range(1,n):  #!行列分清，不要弄反了
            for j in range(1,m):
                dp[j][i]=dp[j-1][i]+dp[j][i-1]

        return dp[m-1][n-1]

