from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head

        while fast and fast.next:  #1.fast要先判空  2.fast!=slow 有问题：初始条件就是fast==slow，直接不执行！
            fast=fast.next.next
            slow=slow.next
            if fast==slow:  #! 学习思路写法
                break
        if not fast.next:
            return None

        index1=fast
        index2=head
        while index1!=index2:
            index1=index1.next
            index2=index2.next
        return index1


