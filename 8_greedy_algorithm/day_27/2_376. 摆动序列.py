from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        result=1
        prediff=0

        for i in range(len(nums)-1):
            curdiff=nums[i+1]-nums[i]
            if (prediff<=0 and curdiff>0) or (prediff>=0 and curdiff<0):
                result+=1
                prediff=curdiff   #!③单调坡中有平坡:在if里
        return result

