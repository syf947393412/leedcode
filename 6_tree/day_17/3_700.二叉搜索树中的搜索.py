from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            p = self.searchBST(root.left, val)
            if p and p.val == val:
                return p
        if root.val < val:
            p = self.searchBST(root.right, val)
            if p and p.val == val:
                return p

        return None


