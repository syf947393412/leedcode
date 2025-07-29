class Solution:
    def isHappy(self, n: int) -> bool:
        record_set=set()

        while n not in record_set:
            record_set.add(n)   #!写这段代码的位置！在模拟一遍
            sum=0
            for i in str(n):
                sum+=int(i)**2
            if sum ==1:
                return True
            # record_set.add(n)    vs
            n=sum
        return False


s=Solution()
a=s.isHappy(n=19)
print(a)
