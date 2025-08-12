from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.left==None and root.right==None:
            if val <root.val:
                root.left=TreeNode(val=val)
            elif val>root.val:
                root.right=TreeNode(val=val)

        if val<root.val:
            self.insertIntoBST(root.left,val)
        if val>root.val:
            self.insertIntoBST(root.right,val)
        return root
