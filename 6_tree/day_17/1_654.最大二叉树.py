from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums is None or len(nums)==0:  #!①left_nums = nums[:0] = [] ← 空列表！
            return None                   #  ②if nums is None:  vs  if not nums:

        max_num=max(nums)
        max_index=nums.index(max_num)
        root=TreeNode(val=max_num)

        left_nums=nums[:max_index]
        right_nums=nums[max_index+1:]

        root.left=self.constructMaximumBinaryTree(left_nums)
        root.right=self.constructMaximumBinaryTree(right_nums)

        return root

