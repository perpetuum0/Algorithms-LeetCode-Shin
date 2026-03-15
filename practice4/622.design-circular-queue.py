#
# @lc app=leetcode id=622 lang=python
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None for _ in range(k)]
        self.start=0
        self.items=0
        self.size = k

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.items>=self.size:
            return False
        else:
            pos = self.start+self.items
            if pos>=len(self.q):
                pos=pos-len(self.q)
            self.q[pos] = value
            self.items+=1
            return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.items<=0:
            return False
        else:
            self.start+=1
            if self.start>=len(self.q):
                self.start=0
            self.items-=1
            return True

    def Front(self):
        """
        :rtype: int
        """
        if self.items<=0:
            return -1
        else:
            return self.q[self.start]

    def Rear(self):
        """
        :rtype: int
        """
        if self.items<=0:
            return -1
        else:
            pos = self.start+self.items-1
            if pos>=len(self.q):
                pos=pos-len(self.q)
            return self.q[pos]

    def isEmpty(self):
        return self.items<=0

    def isFull(self):
        return self.items>=self.size



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

