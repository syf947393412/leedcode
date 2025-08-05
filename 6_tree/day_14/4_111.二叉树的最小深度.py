from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left==None and root.right==None:
            deep=1
        elif root.left==None and root.right!=None:  #!写的时候不要粗心！！！不然不好找错
            deep=self.minDepth(root.right)+1

        elif root.left!=None and root.right==None:
            deep=self.minDepth(root.left)+1
        elif root.left!=None and root.right!=None:
            left_deep=self.minDepth(root.left)
            right_deep=self.minDepth(root.right)
            deep=min(left_deep,right_deep)+1

        return deep
