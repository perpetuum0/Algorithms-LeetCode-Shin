#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = []
        fresh_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
            
        minutes_passed = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue and fresh_count > 0:
            minutes_passed += 1
            next_queue = []
            for r, c in queue:
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        next_queue.append((nr, nc))
            queue = next_queue
            
        return minutes_passed if fresh_count == 0 else -1
# @lc code=end

