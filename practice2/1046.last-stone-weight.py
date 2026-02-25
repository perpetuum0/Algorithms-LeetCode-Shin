#
# @lc app=leetcode id=1046 lang=python
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution(object):
    def max_heapify(self, arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(arr, n, i)
            
        return arr

    def sift_down(self, arr, n, i):
        largest = i
        left_child = 2 * i + 1   
        right_child = 2 * i + 2  

        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.sift_down(arr, n, largest)    
    
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        sh=self.max_heapify(stones)
        
        while sh>1:
            y=sh[0]
            if len(sh)>1:
                sh[0]=sh.pop()
            else:
                return sh[0]
            self.sift_down(sh, len(sh), 0)
            x=sh[0]
            
            if x==y:
                if len(sh)>1:
                    sh[0]=sh.pop()
                else:
                    return 0
            else:
                sh[0]=y-x
            self.sift_down(sh, len(sh), 0)
        return sh[0]

# @lc code=end

