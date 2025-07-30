from builtins import str


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list=list(s)
        for i in range(len(s),2*k):
            #！错误写法： s[i:i+k+1]=s[i:i+k+1:-1]
            s[i:i + k + 1] = s[i:i + k + 1][::-1]
        s="".join(s_list)   #!
        return s

s=Solution()
str = "abcdefg"
k = 2
a=s.reverseStr(str,k)
print(a)

