class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p=[0 for i in range(26)]   #!变量命名


        for char in s:
            p[ord(char)-ord('a')]+=1  #!ord()：计算ASCII码值
        for char in t:
            p[ord(char)-ord('a')]-=1
        for i in range(26):
            if p[i]!=0:
                return False
        return True
