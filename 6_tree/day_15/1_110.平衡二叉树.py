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
        if self.getHeight(root)==-1:
            return False
        else:
            return True

    def getHeight(self,root):
        if root is None:
            return 0

        left=self.getHeight(root.left)
        if left==-1:
            return -1
        right=self.getHeight(root.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        else:
            return 1+max(left,right)



