from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:abs(x),reverse=True)

        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=nums[i]*(-1)
                k-=1
                if k==0:
                    break
        if k%2==1:
            nums[-1]=nums[-1]*(-1)
        return sum(nums)

s=Solution()
nums = [4,2,3]
k=1
print(s.largestSumAfterKNegations(nums,k))