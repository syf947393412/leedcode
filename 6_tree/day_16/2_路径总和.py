from operator import truediv
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sum = 0      #！vs get_path_sum(root,sum=0)
        self.result=False




        def get_path_sum(root):
            if root is None:
                return

            if root.left==None and root.right==None and self.sum+root.val==targetSum:
                self.result=True
                return     #！


            if root.left:
                self.sum+=root.val
                get_path_sum(root.left)
                self.sum-=root.val
            if root.val:
                self.sum+=root.val
                get_path_sum(root.right)
                self.sum-=root.val
            return
                    

        get_path_sum(root)
        return self.result


