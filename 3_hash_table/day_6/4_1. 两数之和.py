from typing import List


class Solution:
    #暴力解:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record_dict={}
        for index,num in enumerate(nums):   #!enumerate的应用
            temp=target-num
            if temp in record_dict:
                return [index,record_dict[temp]]
            record_dict[num]=index
        return []
