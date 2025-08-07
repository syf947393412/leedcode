from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        current=dummy_head

        while current.next and current.next.next:
            pre=current.next.next
            post=current.next
            post.next =pre.next   #!pre一个指针，可以用来指两个位置
            current.next=pre
            pre.next=post
            current=post

        return dummy_head.next















