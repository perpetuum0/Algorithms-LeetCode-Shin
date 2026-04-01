#
# @lc app=leetcode id=450 lang=python
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minimum(self, root):
        r=root
        while r and r.left:
            r=r.left
        return r

    def search(self, root, key):
        r = root
        while r and r.val != key:
            if r.val > key:
                r=r.left
            else:
                r=r.right
        return r

    def parentByKey(self, root, key):
        r = root
        while r:
            if r.left and r.left.val == key or r.right and r.right.val == key:
                return r
            if r.val > key:
                r=r.left
            else:
                r=r.right
        return None

    def deleteNode(self, root, key):
        node = self.search(root,key)
        p = self.parentByKey(root, key)
        
        if not node:
            return root

        if not node.left and not node.right:
            if not p:
                return None
            if p.val>key:
                p.left = None
            else:
                p.right = None
        elif node.left and node.right:
            s = self.minimum(node.right)
            self.deleteNode(root,s.val)
            s.left=node.left
            s.right=node.right
            if not p:
                return s
            if p.val>key:
                p.left = s
            else:
                p.right = s
        else:
            child=node.left if node.left else node.right
            if not p:
                return child
            if p.val>key:
                p.left = child
            else:
                p.right = child
        return root
# @lc code=end

