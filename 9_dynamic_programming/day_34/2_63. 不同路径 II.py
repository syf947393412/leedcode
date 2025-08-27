from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) :
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        # dp=[[0]*n]*m
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            if obstacleGrid[0][i]==1:
                break
            else:
                dp[0][i]=1

        for j in range(m):
            if obstacleGrid[j][0]==1:
                break
            else:
                dp[j][0]=1

        # for j in range(m):
        for j in range(1,m):
            for i in range(1,n):
                if obstacleGrid[j][i]==1:
                    continue
                else:
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]

        return dp[m-1][n-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
so=Solution()
print(so.uniquePathsWithObstacles(obstacleGrid))