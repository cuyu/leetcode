#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#


# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        # dp(n) = dp(n-1) + dp(n-2)
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


# @lc code=end
if __name__ == "__main__":
    Solution().fib(4)
