from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def compare(left,right):  #!
            if not left and right:
                return False
            elif left and not right:
                return False
            elif not left and not right:
                return True
            elif left.val !=right.val:
                return False
            left_left_bool=compare(left.left,right.right)  #!
            left_right_bool=compare(left.right,right.left)

            if left_left_bool and left_right_bool:
                return True
            else:             #!
                return False
        compare(root.left,root.right)