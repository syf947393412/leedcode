class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list=[0]*26
        for char in magazine:
            list[ord(char)-ord('a')]+=1
        for char in ransomNote:
            list[ord(char)-ord('a')]-=1
        for i in list:
            if i <=-1:
                return False
        return True