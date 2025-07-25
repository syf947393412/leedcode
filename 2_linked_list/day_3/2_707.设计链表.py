"""单链表"""
class ListNode:    #!
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyLinkedList:
    def __init__(self):
        self.dummy_head=ListNode()    #!
        self.size=0   #!
    def get(self, index: int) -> int:
        if index<0 and index>=self.size:  #！先判异常赋值
            return -1
        current=self.dummy_head.next
        for i in range(index):
            current=current.next
        return current.val
    def addAtHead(self, val: int) -> None:
        new_head=ListNode(val=val,next=self.dummy_head.next)
        self.dummy_head.next=new_head
        self.size+=1         #!
        # return self.dummy_head      #!

    def addAtTail(self, val: int) -> None:
        current=self.dummy_head
        while current.next:
            current=current.next

        current.next=ListNode(val=val)
        self.size+=1     #!

    def addAtIndex(self, index: int, val: int) -> None:
        if index==self.size:
            self.addAtTail(val)

        elif index>=0 and index<self.size:
            current = self.dummy_head
            for i in range(index):
                current=current.next
            new_node=ListNode(val=val,next=current.next)
            current.next=new_node
            self.size+=1
        else:
            return
    def deleteAtIndex(self, index: int) -> None:
        if index<0 and index>=self.size:
            return
        current=self.dummy_head
        for i in range(index):
            current=current.next
        current.next=current.next.next
        self.size-=1



