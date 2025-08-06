from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left==None and root.right==None:
            return 0

        left_sum=self.sumOfLeftLeaves(root.left)
        if root.left!=None and root.left.left==None and root.left.right==None:
            left_sum=root.left.val

        right_sum=self.sumOfLeftLeaves(root.right)
        sum=left_sum+right_sum
        return sum



