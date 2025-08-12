class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        if root==p or root==q:
            return root


        left_child=self.lowestCommonAncestor(root.left,p,q)
        right_child=self.lowestCommonAncestor(root.right,p,q)

        if left_child==None and right_child!=None:
            return right_child
        elif left_child!=None and right_child==None:
            # return right_child    #!粗心
            return left_child
        elif left_child!=None and right_child!=None:
            return root
        else:
            return None

