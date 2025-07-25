# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)  #！

        p=dummy_head

        while p.next:  #！vs p.next!=None
            if p.next.val==val:
                p.next=p.next.next
                # p=p.next       #！

            else:              #！
                p=p.next

        return dummy_head.next





