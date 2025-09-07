from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]

        for i in range(len(nums1)+1):
            dp[0][i]=0

        for j in range(len(nums2)+1):
            dp[j][0]=0

        result=0
        for i in range(1,len(nums2)+1):
            for j in range(1,len(nums1)+1):
                if nums1[j-1]==nums2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    result=max(result,dp[i][j])

        return result

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
so=Solution()
print(so.findLength(nums1,nums2))
