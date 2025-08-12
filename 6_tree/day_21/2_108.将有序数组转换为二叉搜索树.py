
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def traversal(nums,left,right):
            if left>right:  #!为什么不是>=:如果是等于，即数组里有一个数，还需要继续构造二叉树
                return None
            mid=(left+right)//2
            root=TreeNode(val=nums[mid])

            root.left=traversal(nums,left,mid-1)
            root.right=traversal(nums,mid+1,right)
            return root
        return traversal(nums,0,len(nums)-1)


