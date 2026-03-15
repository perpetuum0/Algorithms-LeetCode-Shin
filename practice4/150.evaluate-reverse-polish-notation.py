#
# @lc app=leetcode id=150 lang=python
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {
            '+': (lambda a, b: a+b),
            '-': (lambda a, b: a-b),
            '*': (lambda a, b: a*b),
            '/': (lambda a, b: int(a / b))
        }
        
        st=[]
        
        for token in tokens:
            if token in ops:
                b = st.pop()
                a = st.pop()
                st.append(ops[token](a, b))
            else:
                st.append(int(token))
        return st[0]
# @lc code=end

