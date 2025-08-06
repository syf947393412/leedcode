from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     count_left=self.countNodes(root.left)
    #     count_right=self.countNodes(root.right)
    #     count=count_left+count_right+1
    #     return count
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth=0
        right_depth=0
        left=root.left
        right=root.right
        while left:
            left=left.left
            left_depth+=1
        while right:
            right=right.right
            right_depth+=1
        if left_depth==right_depth:
            nodes_count=(2 << left_depth) - 1   #!
            return nodes_count
        left_count=self.countNodes(root.left)
        right_count=self.countNodes(root.right)
        count=left_count+right_count+1
        return count