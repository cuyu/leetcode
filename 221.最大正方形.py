#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp(i,j)表示以i，j为右下角可能存在的最大正方形边长
        # if matrix[i,j] == 1:
        # dp(i,j) = dp(i-1,j) + 1 当dp(i-1,j) == dp(i,j-1)且matrix[i-dp(i-1,j), j-dp(i-1,j)] == 1
        # dp(i,j) = dp(i-1,j)     当dp(i-1,j) == dp(i,j-1)且matrix[i-dp(i-1,j), j-dp(i-1,j)] == 0
        # dp(i,j) = min(dp(i-1,j), dp(i,j-1)) + 1 其他情况
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0] * width for _ in range(height)]
        for i in range(height):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        for i in range(width):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        for i in range(1, height):
            for j in range(1, width):
                if matrix[i][j] == '0':
                    continue
                if dp[i-1][j] == dp[i][j-1]:
                    if matrix[i-dp[i-1][j]][j-dp[i-1][j]] == '1':
                        dp[i][j] = dp[i-1][j] + 1
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        tmp = [max(x) for x in dp]
        return max(tmp) ** 2

# @lc code=end


if __name__ == "__main__":
    Solution().maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
        "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
