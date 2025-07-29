from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record_dict={}
        for n1 in nums1:
            for n2 in nums2:
                #!错误写法：当 n1+n2 的值不在字典中时，直接访问会抛出 KeyError。
                # if record_dict[n1+n2]:
                #     record_dict[n1 + n2] += 1
                sum=n1+n2
                if sum in record_dict:
                    record_dict[sum]+=1
                else:
                    record_dict[sum]=1
        count=0    #!
        for n3 in nums3:
            for n4 in nums4:
                sum2=-(n3+n4)
                if sum2 in record_dict:
                    #!错误写法：
                    # return record_dict[sum2]
                    count+=record_dict[sum2]
        return count








s = Solution()
a = s.isHappy(n=19)
print(a)



