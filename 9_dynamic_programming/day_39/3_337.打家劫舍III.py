from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result=self.traversal(root)
        return max(result[0],result[1])

    def traversal(self,root):
        if root is None:
            return (0,0)

        left=self.traversal(root.left)
        right=self.traversal(root.right)

        dp=[0]*2
        dp[0]=max(left[0],left[1])+max(right[0],right[1])
        dp[1]=root.val+left[0]+right[0]
        return (dp[0],dp[1])



