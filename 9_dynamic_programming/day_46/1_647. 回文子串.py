class Solution:
    def countSubstrings(self, s: str) -> int:
        dp=[[False for _ in range(len(s))] for _ in range(len(s))]

        result=0
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j]:
                    if i==j or j==i+1:
                        dp[i][j]=True
                        result+=1
                    elif j-i>1 and dp[i+1][j-1]==True:
                        dp[i][j]=True
                        result+=1

        return result
