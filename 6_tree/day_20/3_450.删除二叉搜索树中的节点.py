from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root ==None:
            return None
        elif root.left==None and root.right==None and root.val==key:
            return root.left
        elif root.left!=None and root.right==None and root.val==key:
            return root.left
        elif root.left==None and root.right!=None and root.val==key:
            return root.right
        elif root.left!=None and root.right!=None and root.val==key:
            cur=root.right
            while cur:
                cur=cur.left
            cur.left=root.left
            return root.right
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        if root.val<key:
            root.right=self.deleteNode(root.right,key)
        return root


