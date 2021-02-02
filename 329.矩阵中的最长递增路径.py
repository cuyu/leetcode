#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        d = [[-1] * width for _ in range(height)]

        def dfs(i: int, j: int) -> int:
            if d[i][j] != -1:
                return d[i][j]
            cur = matrix[i][j]
            length = []
            if i-1 >= 0 and matrix[i-1][j] > cur:
                length.append(1 + dfs(i-1, j))
            if j-1 >= 0 and matrix[i][j-1] > cur:
                length.append(1 + dfs(i, j-1))
            if i+1 < height and matrix[i+1][j] > cur:
                length.append(1 + dfs(i+1, j))
            if j+1 < width and matrix[i][j+1] > cur:
                length.append(1 + dfs(i, j+1))
            if length:
                r = max(length)
            else:
                r = 1
            d[i][j] = r
            return r

        longest = 0
        for i in range(height):
            for j in range(width):
                l = dfs(i, j)
                if l > longest:
                    longest = l
        return longest
# @lc code=end
