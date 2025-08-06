from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root)==-1:
            return False
        else:
            return True

    def get_height(self,root):
        if root is None:
            return -1
        left_height=self.get_height(root.left)
        if left_height==-1:
            return -1
        right_height=self.get_height(root.right)
        if right_height==-1:
            return -1

        # elif abs(left_height-right_height)<2:  #!
        if abs(left_height-right_height)>1:
            return -1

        height=max(left_height,right_height)+1
        return height

