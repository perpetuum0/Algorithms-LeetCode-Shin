#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        full = set(nums1+nums2)
        nums1 = set(nums1)
        nums2 = set(nums2)

        leftOuter = nums1-nums2
        rightOuter = nums2-nums1

        inner = full - leftOuter - rightOuter

        return list(inner)
# @lc code=end

