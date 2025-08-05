from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left_height=self.maxDepth(root.left)   #左
        right_height=self.maxDepth(root.right)   #右
        max_deep=1+max(left_height,right_height)   #中    ——>后序遍历
        return max_deep
