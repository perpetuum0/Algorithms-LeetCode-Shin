#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.mins)==0 or val <= self.mins[-1]:
            self.mins.append(val)

    def pop(self):
        """
        :rtype: None
        """
        p = self.stack.pop()
        if len(self.mins)>0 and p == self.mins[-1]:
            self.mins.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return None if len(self.mins)==0 else self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

