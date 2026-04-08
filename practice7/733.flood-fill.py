#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, toFill=None) -> List[List[int]]:
        if sr>=0 and sr<len(image) and sc>=0 and sc<len(image[sr]):
            toFill = toFill if toFill is not None else image[sr][sc]
            if toFill != color and image[sr][sc] == toFill:
                image[sr][sc]=color
                self.floodFill(image, sr+1, sc, color, toFill)
                self.floodFill(image, sr-1, sc, color, toFill)
                self.floodFill(image, sr, sc-1, color, toFill)
                self.floodFill(image, sr, sc+1, color, toFill)
        return image
# @lc code=end

