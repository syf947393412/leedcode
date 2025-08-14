from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre=0  #!pre 是int，只记录前一个的数据就可以了
        def traversal(root):
            if root is None:
                return     #!

            traversal(root.right)
            root.val+=self.pre
            self.pre=root.val
            traversal(root.left)

            return root
        return traversal(root)
