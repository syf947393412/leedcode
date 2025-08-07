from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth=float("-inf")   #!
        self.result=0   #!self.
        def get_left_leaf(node,depth):
            if node.left==None and node.right==None:
                if depth>self.max_depth:
                    self.result=node.val
                    self.max_depth=depth
            if node.left:
                depth+=1
                get_left_leaf(node.left,depth)
                depth-=1
            if node.right:
                depth+=1
                get_left_leaf(node.right,depth)
                depth-=1

        get_left_leaf(root,depth=0)
        return self.result
