from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    #不增加空间复杂度后的思路！
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        current = head


        while current:
            p=current.next
            current.next=temp
            temp=current
            current=p
        return temp






