#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i,j]表示从第i个元素到第j个元素组成的子串是否是回文子串
        if len(s) < 2:
            return s
        dp = [[False] * len(s) for _ in range(len(s))]

        # 初始化
        for i in range(len(s)):
            # 单个字符肯定是回文串
            dp[i][i] = True
        for i in range(len(s) - 1):
            # 两个字符的情况
            dp[i][i+1] = (s[i] == s[i+1])

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False
        longest = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i][j] and j - i + 1 > len(longest):
                    longest = s[i: j + 1]
        return longest
# @lc code=end


if __name__ == "__main__":
    Solution().longestPalindrome("aaa")
