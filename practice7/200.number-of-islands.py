#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def fill(self, grid, sr, sc, newVal, toFill) -> List[List[int]]:
        if sr>=0 and sr<len(grid) and sc>=0 and sc<len(grid[sr]):
            if toFill != newVal and grid[sr][sc] == toFill:
                grid[sr][sc]=newVal
                self.fill(grid, sr+1, sc, newVal, toFill)
                self.fill(grid, sr-1, sc, newVal, toFill)
                self.fill(grid, sr, sc-1, newVal, toFill)
                self.fill(grid, sr, sc+1, newVal, toFill)

    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    self.fill(grid, i, j, '2', '1')
                    count+=1
        return count
# @lc code=end

