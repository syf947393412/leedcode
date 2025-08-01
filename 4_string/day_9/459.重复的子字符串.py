from typing import List


def getNext(s:str):
    j = 0
    next=[0]*len(s)
    for i in range(1,len(s)):
        while j>0 and s[j]!=s[i]:
            j=next[j-1]
        if s[j]==s[i]:
            j+=1
        next[i]=j
    print(next)

s="aabaaf"
getNext(s=s)


