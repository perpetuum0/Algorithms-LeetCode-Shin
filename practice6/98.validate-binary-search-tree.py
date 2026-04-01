#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self, rt, min, max):
        if not rt:
            return True
        elif not min<rt.val<max:
            return False
        
        return self.check(rt.left, min, rt.val) and self.check(rt.right, rt.val, max)
    
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.check(root, float('-inf'), float('inf'))
# @lc code=end

