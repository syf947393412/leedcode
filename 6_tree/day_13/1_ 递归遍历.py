from typing import List


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def dfs(node:TreeNode):
            if node is None:
                return    #!

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return result

