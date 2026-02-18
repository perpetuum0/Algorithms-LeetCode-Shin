#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        
        while l!=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                r=m-1
            else: 
                l=m+1
            if m<=0:
                break
        
        return (l if nums[l]==target else -1)

        # @lc code=end
        