from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record_dict={}
        for item in nums:
            # if record_dict[item]:    #!
            if item in record_dict:
                record_dict[item]+=1
            else:
                record_dict[item]=1
        dict={}
        # for key,value in record_dict:   #!
        for key,value in record_dict.items():
            # if dict[value]:     #!
            if value in dict:
                dict[value].append(key)
            else:
                dict[value]=[key]
        # list=list(dict.keys())   #!用 list 作为变量名，但 list 是Python的内置类型。这会覆盖内置的 list 函数。
        result_list=list(dict.keys())   #!

        # list_sort=result_list.sort()   #！ list.sort() 方法是就地排序，它直接修改原列表并返回 None
                                        #！vs  sorted(result_list)
        result_list.sort(reverse=True)     #!由高到低排序

        count=0
        result=[]
        i=0
        while count<k:
            result+=dict[result_list[i]]
            count+=len(dict[result_list[i]])  #!理解含义
            i+=1
        return result




s=Solution()
nums=[1,1,1,2,2,3]
# nums.sort()
# print(nums)
k=2
result=s.topKFrequent(nums=nums,k=k)
print(result)
