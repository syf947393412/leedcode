from typing import List

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n_list=list(str(n))

        flag=len(n_list)  #!没有初始化为0的原因：特例1000

        for i in range(len(n_list)-1,0,-1):
            if int(n_list[i])<int(n_list[i-1]):
                n_list[i-1]=str(int(n_list[i-1])-1)
                flag=i   #！为什么标记flag，而不是n_list[i]="9"   :特例1000
        for i in range(flag,len(n_list)):
            n_list[i]="9"

        return int("".join(n_list))


