#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution(object):
    def min_heapify(self,arr):
        n = len(arr)
        
        for i in range(n // 2 - 1, -1, -1):
            self.sift_down(arr, n, i)
            
        return arr

    def sift_down(self,arr, n, i):
        smallest = i
        left_child = 2 * i + 1   
        right_child = 2 * i + 2  

        if left_child < n and arr[left_child][1] < arr[smallest][1]:
            smallest = left_child

        if right_child < n and arr[right_child][1] < arr[smallest][1]:
            smallest = right_child

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.sift_down(arr, n, smallest)
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        pd=[]
        for p in points:
            pd.append((p, pow((p[0]**2 + p[1]**2), 0.5)))
            
        self.min_heapify(pd)
        ans=[]
        d=0
        while d<k:
            ans.append(pd[0][0])
            if len(pd)<=1:
                break
            pd[0]=pd.pop()
            self.sift_down(pd, len(pd), 0)
            d+=1

        return ans
# @lc code=end

