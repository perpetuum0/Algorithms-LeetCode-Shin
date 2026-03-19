#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

# @lc code=start
class Solution(object):
    def countLetters(self, s):
        res={}
        for l in s:
            if l in res:
                res[l]+=1
            else:
                res[l]=1
        return res

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.countLetters(s) == self.countLetters(t)
# @lc code=end

