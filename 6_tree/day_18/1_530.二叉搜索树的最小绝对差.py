from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min=10000000  #！min 和 pre 是局部变量，递归调用时每层都有自己的副本，无法在递归间共享状态
        self.pre=None
        def traversal(root):
            if root is None:
                return 0

            self.getMinimumDifference(root.left)
            if self.pre and (root.val-self.pre.val)<self.min:
                self.min=root.val-self.pre.val
            self.pre=root
            self.getMinimumDifference(root.right)
        traversal(root)
        return self.min

