from typing import Optional
#!难题

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val<low:
            right=self.trimBST(root.right,low,high)
            return right
        if root.val>high:
            left=self.trimBST(root.left,low,high)
            return left

        #! 对上一层的处理
        root.left=self.trimBST(root.left,low,high)
        root.right=self.trimBST(root.right,low,high)
        return root