class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        pre=dummy_head
        current=dummy_head

        for i in range(n):
            pre=pre.next

        while pre.next:
            pre=pre.next
            current=current.next
        current.next=current.next.next
        return dummy_head.next