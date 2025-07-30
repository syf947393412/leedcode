from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=len(s)
        final=len(s)//2
        for i in range(final):
            front=s[i]
            back=s[l-i-1]
            s[i]=back
            s[l-i-1]=front
        return s