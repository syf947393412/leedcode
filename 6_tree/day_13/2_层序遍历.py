from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:#!
            return []
        result=[]
        queue=deque([root])  #![root]:deque需要iterable

        while queue:
            level = []
            for i in range(len(queue)):  #!len(queue)=每层元素数
                temp=queue.popleft()
                level.append(temp.val)
                if temp.left is not None:    #！
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            result.append(level)
        return result

