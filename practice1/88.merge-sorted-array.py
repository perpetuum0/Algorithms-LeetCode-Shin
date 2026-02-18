#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        s=m
        for x in nums2:
            j=s-1
            while j>=0 and nums1[j]>x:
                
                nums1[j+1]=nums1[j]
                j-=1
            nums1[j+1]=x
            s+=1
# @lc code=end

