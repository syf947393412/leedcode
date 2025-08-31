from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #！ s字符串是背包

        dp=[False]*(len(s)+1)
        dp[0]=True
        word_set=set(wordDict)

        for j in range(1,len(s)+1):  #背包
            # for i in range(len(s)):
            for i in range(j):  #遍历单词
                # if dp[i] and s[i:j+1] in word_set:
                if dp[i] and s[i:j] in word_set:
                    dp[j]=True

        return dp[len(s)]

