from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]表示有amount为i时所需的最少的硬币个数
        # dp[i] = min(dp[i-k]) + 1,其中k为coins里的各个元素
        if amount == 0:
            return 0
        dp = [-1] * (amount + 1)
        coins_set = set(coins)
        for i in range(1, amount + 1):
            if i in coins_set:
                dp[i] = 1
            else:
                min_tmp = amount + 1
                for k in coins:
                    p = i - k
                    if p >= 0 and dp[p] > 0:
                        if dp[p] < min_tmp:
                            min_tmp = dp[p]
                if min_tmp != (amount + 1):
                    dp[i] = min_tmp + 1
                else:
                    dp[i] = -1
        return dp[-1]


if __name__ == "__main__":
    Solution().coinChange([2], 3)
