#
# @lc app=leetcode id=912 lang=python
#
# [912] Sort an Array
#

# @lc code=start
class Solution(object):
    def sort(self, nums):
        if len(nums)<=1:
            return nums
        
        l = self.sort(nums[0 : len(nums)//2])
        r = self.sort(nums[len(nums)//2 : len(nums)])
        return self.merge(l, r)
    
    def merge(self, a, b):
        i, j = 0, 0
        result = []
        while i<len(a) and j<len(b):
            if(a[i]<=b[j]):
                result.append(a[i])
                i+=1
            else:
                result.append(b[j])
                j+=1
        
        while i<len(a):
            result.append(a[i])
            i+=1
        while j<len(b):
            result.append(b[j])
            j+=1
        
        return result
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.sort(nums)
        
# @lc code=end

