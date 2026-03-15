#
# @lc app=leetcode id=707 lang=python
#
# [707] Design Linked List
#

# @lc code=start
class Node(object):
    def __init__(self, val, prev, next):
        self.val=val
        self.prev=prev
        self.next=next

class MyLinkedList(object):
    def __init__(self):
        self.origin=None

    def get(self, index):
        n=self.origin
        while index>0 and n.next:
            n=n.next
            index-=1
        if index==0 and n:
            return n.val
        else:
            return -1

    def addAtHead(self, val):
        if self.origin is None:
            self.origin = Node(val, None, None)
        else:
            self.origin.prev=Node(val, None, self.origin)
            self.origin=self.origin.prev

    def addAtTail(self, val):
        if self.origin is None:
            self.origin = Node(val, None, None)
        else:
            n=self.origin
            while n.next is not None:
                n=n.next
            n.next=Node(val, n, None)

    def addAtIndex(self, index, val):
        if index==0 and not self.origin:
            self.origin = Node(val, None, None)
        else:
            prev=None
            n=self.origin
            while index>0:
                if n is None:
                    return
                prev=n
                n=n.next
                
                index-=1
            
            new_node = Node(val, None, None)
            if n==self.origin:
                    self.origin=new_node
            if n:
                n.prev=new_node
                new_node.next=n
            if prev:
                prev.next=new_node
                new_node.prev=prev

    def deleteAtIndex(self, index):
        if index==0:
            if not self.origin:
                return None
            elif self.origin.next:
                self.origin=self.origin.next
            else: self.origin=None
        else:
            n=self.origin
            while index>0 and n.next:
                n=n.next
                index-=1
                
            if index==0:
                if n.next and n.prev:
                    n.prev.next=n.next
                    n.next.prev=n.prev
                elif n.prev:
                    n.prev.next=None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

