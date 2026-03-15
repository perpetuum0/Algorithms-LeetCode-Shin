#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = []
        
        matches = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        
        for ch in s:
            if ch in list(matches.keys()):
                if len(st)>0 and st[len(st)-1] == matches[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
                
        return len(st)==0
# @lc code=end

