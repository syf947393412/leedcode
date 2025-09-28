from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left==None and root.right==None:
            return True
        if root.val<root.left.val or root.val>root.right.val:
            return False

        left_bool=self.isValidBST(root.left)
        right_bool=self.isValidBST(root.right)
        if left_bool and right_bool and root.val>root.left.val and root.val<root.right.val:
            return True
        return False

















