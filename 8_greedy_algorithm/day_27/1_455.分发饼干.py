
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()   #!
        g.sort()

        result=0
        index=len(s)-1
        # for i in range(len(g)-1,0,-1):   #!
        for i in range(len(g)-1,-1,-1):
            if index>0 and s[index]>=g[i]:   #!
                index-=1                     #! ↑
                result+=1
        return result

so=Solution()
g=[1,2,7,10]
s=[1,3,5,9]
result=so.findContentChildren(g,s)
print(result)