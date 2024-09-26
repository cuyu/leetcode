#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # dp(n) = 1 + min(dp(n - coins[0]), dp(n - coins[1]), ...)
        dp = [-1] * (amount + 1)
        coins_set = set(coins)
        min_coin = min(coins_set)
        for c in coins:
            if c < len(dp):
                dp[c] = 1
        for i in range(min_coin + 1, len(dp)):
            if i not in coins_set:
                tmp = list(
                    filter(lambda x: x != -1, [dp[max(i - c, 0)] for c in coins])
                )
                dp[i] = 1 + min(tmp) if tmp else -1
        return dp[amount]


# @lc code=end
if __name__ == "__main__":
    Solution().coinChange([2], 3)
