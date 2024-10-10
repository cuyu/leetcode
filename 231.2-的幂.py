#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n // 2)


# @lc code=end
