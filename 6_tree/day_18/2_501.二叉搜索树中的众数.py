from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.max_count=0
        self.result=[]
        self.count=0
        self.pre=None

        def traversal(root):
            if root is None:
                return []
            traversal(root.left)
            if self.pre is None:
                self.count=1   #!
            elif self.pre and root.val==self.pre.val:
                self.count+=1
            else:
                self.count=1   #!
            if self.count==self.max_count:
                self.result.append(root.val)
            elif self.count>self.max_count:
                self.max_count=self.count
                self.result=[]
                self.result.append(root.val)
            self.pre=root   #!缺少 self.pre 的更新
            traversal(root.right)

            return
        traversal(root)
        return self.result
