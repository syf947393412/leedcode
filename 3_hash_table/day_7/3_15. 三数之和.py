from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()    #!sort():nums=[-1,0,1,2,-1,-4] -->nums=[-1,-1,-1,0,1,2]

        for i in range(len(nums)):
            if nums[i]>0:   #!
                return result
            if i>0 and nums[i]==nums[i-1]: #!去重：对比为什么不用nums[i]==nums[i+1] （用i+1首次出现也不会记录进结果）
                continue

            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]<0:
                    left+=1
                elif nums[i]+nums[left]+nums[right]>0:
                    right-=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    #！ 错误写法： while left<right and nums[left]==nums[left-1]:  #!去重
                    while left<right and nums[left]==nums[left+1]:  #!去重
                        left+=1
                    #错误写法： while left<right and nums[right]==nums[right+1]:      IndexError: list index out of range
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left += 1
                    right -= 1


        return result



s = Solution()
nums = [-1,0,1,2,-1,-4]
a = s.threeSum(nums=nums)
print(a)
