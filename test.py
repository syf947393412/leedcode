from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [0] * len(nums)
        self.backtracing(nums, [], result, used)  #
        return result

    def backtracing(self, nums, path, result, used):  #
        if len(path) == len(nums):
            result.append(path)
            return

        for i in range(0, len(nums)):
            if used[i] == 0:
                path.append(nums[i])
                used[i] = 1
                self.backtracing(nums, path, result, used)
                used[i] = 0
                path.pop()

        return

nums = [1,2,3]
so=Solution()
print(so.permute(nums))