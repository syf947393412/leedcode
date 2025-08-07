class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # if len(postorder)==0:   #!
        #     return
        if not postorder:
            return None

        root_val=postorder[-1]
        root=TreeNode(val=root_val)

        i=inorder.index(root_val)

        left_inorder=inorder[:i]
        right_inorder=inorder[i+1:len(inorder)]   #!i+1

        left_postorder=postorder[:len(left_inorder)]
        # right_postorder=postorder[len(left_inorder)+1:len(postorder)-1]
        right_postorder=postorder[len(left_inorder):len(postorder)-1]

        root.left=self.buildTree(left_inorder,left_postorder)
        root.right=self.buildTree(right_inorder,right_postorder)
        return root     #!