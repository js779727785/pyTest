class ListNode():
    def __init__(self,head):
        self.head=head
        self.next=None
class FF():
    def fun(self,listNode,tar):
        dummyNode=ListNode(0)
        dummyNode.next=listNode
        slow,fast=dummyNode
        while tar!=0:
            fast=fast.next
            tar-=1
        while fast!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummyNode.next