from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.left.val>=root.val:
            return False
        if root.right and root.right.val<=root.val:
            return False
        if root.left==None and root.right==None:
            return True

        left_bool=self.isValidBST(root.left)
        right_bool=self.isValidBST(root.right)
        if left_bool and right_bool and root.left.val<root.val and root.right.val>root.val:
            return True