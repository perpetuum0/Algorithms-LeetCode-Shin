#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
from math import factorial
class Solution:
    def climbStairs(self, n: int) -> int:
        varis=0
        b=n
        a=0.0
        while b>=0:
            if a.is_integer():
                varis+=int(factorial(int(a)+b)/(factorial(int(a))*factorial(b)))
            b-=1
            a+=0.5
        
        return varis
# @lc code=end

