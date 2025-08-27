from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        # nums.sort()

        self.backtracing(nums,result,[],0)

        return result

    def backtracing(self,nums,result,path,start_index):
        # if len(path)==2:
        if len(path)>=2:
            # result.append(path)
            result.append(path[:])


        uset=set()  #!去重
        for i in range(start_index,len(nums)):
            #！去重逻辑：①用or   ②nums[i] in uset
            # if i>0 and nums[i]<=nums[i-1] and used[i-1]==0:
            if (path and nums[i]<path[-1]) or nums[i] in uset :
                continue

            path.append(nums[i])
            # used[i]=1   #!
            uset.add(nums[i])  #!set插入用add

            #回溯时，不加uset
            # self.backtracing(nums,result,path,i+1,used)
            self.backtracing(nums,result,path,i+1)

            path.pop()
        return

#==============================================================
class Solution2:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        used=[0]*len(nums)
        result=[]
        self.backtracing(nums,result,[],0)

        return result

    def backtracing(self,nums,result,path,start_index):
        if len(path)>=2:
            result.append(path[:])

        level_used = set()
        for i in range(start_index,len(nums)):
            # if i>0 and nums[i]==nums[i-1] and used[i-1]==0:
            # ↑只有在数组预先排序的情况下才有效。
            #    continue

            # if i>0 and nums[i]<nums[i-1]:
            #  ↑应该是比较当前元素和当前路径 path 中的最后一个元素，以确保子序列是递增的。
            if path and nums[i] < path[-1]:
                continue

            if nums[i] in level_used:
                continue

            path.append(nums[i])
            level_used.add(nums[i])
            self.backtracing(nums,result,path,i+1)

            path.pop()

        return

# nums =[4,6,7,7]
nums = [4,4,3,2,5]

so=Solution2()
print(so.findSubsequences(nums))


