#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def build_max_heap(self, arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(arr, n, i)
            
        return arr

    def _sift_down(self, arr, n, i):
        largest = i
        left_child = 2 * i + 1   
        right_child = 2 * i + 2  

        if left_child < n and arr[left_child][1] > arr[largest][1]:
            largest = left_child

        if right_child < n and arr[right_child][1] > arr[largest][1]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._sift_down(arr, n, largest)
    
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hf={}
        
        for x in nums:
            if x in hf:
                hf[x]+=1
            else:
                hf[x]=1
                
        h=list(hf.items())
        
        self.build_max_heap(h)

        ans=[]
        d=0
        while d<k:
            ans.append(h[0][0])
            if len(h)<=1:
                break
            h[0]=h.pop()
            self._sift_down(h, len(h), 0)
            d+=1
        return ans
# @lc code=end

