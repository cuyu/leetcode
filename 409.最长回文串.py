#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        stats: dict[str, bool] = {}
        # 找出有多少字母是奇数个
        for i in range(len(s)):
            c = s[i]
            if c not in stats:
                stats[c] = True
            else:
                stats[c] = not stats[c]
        count = sum(stats.values())
        return min(len(s), len(s) - count + 1)


# @lc code=end
