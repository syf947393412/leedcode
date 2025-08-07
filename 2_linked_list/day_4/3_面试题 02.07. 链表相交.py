class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def len_link(head:ListNode)->int:
    count=0
    p=head
    while p:
        count+=1
        p=p.next
    return count

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a=len_link(headA)
        len_b=len_link(headB)
        count=len_a-len_b

        a = headA
        b = headB
        if count>0:
            for i in range(count):
                a=a.next
        elif count<0:
            count=abs(count)
            for i in range(count):
                b=b.next

        while a.next and b.next and a.next!=b.next:  #! 需要先判 a.next and b.next！！，然后才能判a.next!=b.next
            a=a.next
            b=b.next
        if not a.next:
            return None
        return a.next     #!最后返回的是ListNode对象