#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue(object):
    def __init__(self):
        self.deq = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        enq = []
        while len(self.deq)>0:
            enq.append(self.deq.pop())
        enq.append(x)
        
        while len(enq)>0:
            self.deq.append(enq.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.deq.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.deq[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.deq)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

