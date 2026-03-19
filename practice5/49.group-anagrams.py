#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm = {}

        for s in strs:
            key = "".join(sorted(list(s)))
            if key in hm:
                hm[key].append(s)
            else: hm[key] = [s]

        return list(hm.values())
        
# @lc code=end

