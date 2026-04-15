#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        visited = set()
        heap = [(0, 0)] 
        
        while len(visited) < len(points):
            cost, i = heapq.heappop(heap)
            if i in visited:
                continue
            result += cost
            visited.add(i)
            for j in range(len(points)):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (dist, j))
                    
        return result
# @lc code=end

