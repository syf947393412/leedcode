from builtins import str
from typing import List


class Solution:
    def getNext(self, next: List[int], s: str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:#j要回退，回退到的地方看next中j的前一位
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        list=[0]*len(needle)
        next=self.getNext(next=list,s=needle)
        j=0
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j=next[j-1]
            if haystack[i]==needle[j]:
                j += 1
            if j==len(needle):
                return i-len(needle)+1
        return -1

s=Solution()
str="aabaaf"
next = [0] * len(str)
next=s.getNext(next,str)
print(next)