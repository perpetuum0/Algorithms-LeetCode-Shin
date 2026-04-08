#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
            
        pq = [(0, k)]
        visited = {}
        
        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited[node] = time
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (time + weight, neighbor))
                    
        return max(visited.values()) if len(visited) == n else -1
# @lc code=end

