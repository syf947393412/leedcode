from operator import invert
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        temp = root
        if temp is None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(temp.left)
        self.invertTree(temp.right)

        return root


