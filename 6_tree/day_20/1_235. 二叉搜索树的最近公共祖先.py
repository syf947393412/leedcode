class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root

        if p.val<root.val and q.val<root.val:
            left=self.lowestCommonAncestor(root.left,p,q)
            if left!=None:
                return left

        if q.val>root.val and p.val>root.val:
            right=self.lowestCommonAncestor(root.right,p,q)
            if right!=None:
                return right

        return root




