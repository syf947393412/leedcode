from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    i=0
    j=0
    sum=0
    min_len= 0

    while i<len(nums):
        while sum<target and j<len(nums):
            sum=sum+nums[j]
            j+=1


        if sum>=target:
            """
            ▲ min_len最开始需要计算一下：

            """
            if min_len==0:
                min_len=j-i
            else:
                min_len=min(min_len,j-i)
        i+=1
        j=i
        sum=0
    return min_len

target = 7
nums = [2,3,1,2,4,3]
# target = 4
# nums = [1,4,4]

# target = 11
# nums = [1,1,1,1,1,1,1,1]

min_len=minSubArrayLen(target,nums)
print(min_len)