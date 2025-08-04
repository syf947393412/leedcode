from typing import List


# def fourSum(nums: List[int], target: int) -> List[List[int]]:
#     record_dict={}
#     result=[]
#     nums.sort()
#     for i in range(len(nums)-3):
#
#         # while j<len(nums)-2 and
#         for j in range(i+1,len(nums)-2):
#
#             left=j+1
#             right=len(nums)-1
#
#             sum=nums[i]+nums[j]
#             if sum in record_dict and record_dict[sum]==[nums[i],nums[j]]:
#                 continue
#             record_dict[sum]=[nums[i],nums[j]]
#             while left<right:
#                 sum2=target-nums[left]-nums[right]
#                 while left+1<right and nums[left+1]==nums[left]:
#                     left+=1
#                 while left<right-1 and nums[right-1]==nums[right]:
#                     right-=1
#                 if sum2==sum:
#                     result.append(record_dict[sum2]+[nums[left],nums[right]])
#                     left+=1
#                     right-=1
#                 elif sum2>sum:
#                     left+=1
#                 else:
#                     right-=1
#     return result

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    result=[]

    for i in range(len(nums)-3):
        #!剪枝：①两个负数相加会更小，所以需要>0的条件
        if nums[i]>target and target>0 and nums[i]>0:
            # return []   #!
            break
        #!去重
        if i>0 and nums[i]==nums[i-1]:
            continue

        for j in range(i+1,len(nums)-2):
            #!剪枝
            if nums[i]+nums[j]>target and target>0 and nums[i]+nums[j]>0:
                # return []
                break
            #!去重
            if j>i+1 and nums[j]==nums[j-1]:
                continue

            left=j+1
            right=len(nums)-1

            while left<right:
                while left>j+1 and nums[left-1]==nums[left]:
                    left+=1
                while right<len(nums)-1 and nums[right]==nums[right+1]:
                    right-=1

                if left<right and nums[i]+nums[j]+nums[left]+nums[right]<target:
                    left+=1
                elif left<right and nums[i]+nums[j]+nums[left]+nums[right]>target:
                    right-=1
                elif left<right and nums[i]+nums[j]+nums[left]+nums[right]==target:
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1  #!
                    right-=1

    return result


nums=[2,2,2,2,2]
target=8
# nums =[1,0,-1,0,-2,2]
# target=0
result=fourSum(nums,target)
print(result)





