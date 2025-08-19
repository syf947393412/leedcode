from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        result=0
        cur=0
        next=0
        i=0
        while i<len(nums):
            next=max(i+nums[i],next)

            if i==cur:
                if cur!=len(nums)-1:
                    result+=1
                    cur = next
                    if cur>=len(nums)-1:
                        break
            i+=1
        return result
s=Solution()
nums=[2,3,1,1,4]
print(s.jump(nums))



