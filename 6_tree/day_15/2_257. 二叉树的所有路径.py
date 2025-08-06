from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        path=[]
        result=[]
        self.traversal(node=root,path=path,result=result)
        return result

    def traversal(self,node:TreeNode,path:List[int],result:List[str]):   #!传入参数的确定
        #中
        path.append(node.val)

        if node.left==None and node.right==None:
            path_str="->".join(map(str,path))
            result.append(path_str)
            return    #!

        #左
        if node.left:
            self.traversal(node.left,path,result)
            path.pop()
        #右
        if node.right:
            self.traversal(node.right,path,result)
            path.pop()
        # return result   #!

