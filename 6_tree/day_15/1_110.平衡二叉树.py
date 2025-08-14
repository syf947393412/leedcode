from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_height=self.isBalanced(root.left)
        right_height=self.isBalanced(root.right)
        height=max(left_height,right_height)+1
        if not left_height or not right_height:
            return False
        elif abs(left_height-right_height)<2:
            return True
        else:
            return False

