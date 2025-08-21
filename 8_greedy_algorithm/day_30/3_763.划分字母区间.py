from typing import List
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash=[0]*26

        #求每个字母的最远位置
        for i in range(len(s)):
            hash[ord(s[i])-ord("a")]=i

        result=[]
        left=0
        right=0
        for i in range(len(s)):
            right=max(right,hash[ord(s[i])-ord("a")])
            if right==i:
                result.append(right-left+1)
                left=right+1

        return result
