#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm={}
        for i in range(len(nums)):
            rem = target-nums[i]
            if rem in hm:
                return i, hm[rem]
            hm[nums[i]] = i
# @lc code=end

