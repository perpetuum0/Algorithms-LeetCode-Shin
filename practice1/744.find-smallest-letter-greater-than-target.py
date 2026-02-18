#
# @lc app=leetcode id=744 lang=python
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for l in letters:
            if ord(l) > ord(target):
                return l
        return letters[0]
# @lc code=end

