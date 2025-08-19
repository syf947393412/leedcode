from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover=1
        """python不支持动态修改for循环中变量,使用while循环代替"""
        # for i in range(cover):   #! i需要在cover范围内移动
        #     cover=max(i+nums[i],cover)
        #     if cover==len(nums)-1:
        #         return True
        #
        # return False
        i=0
        while i<cover:
            cover = max(i + nums[i], cover)
            i+=1
            if cover==len(nums)-1:
                return True

        return False


s=Solution()
nums=[2,3,1,1,4]
print(s.canJump(nums=nums))

