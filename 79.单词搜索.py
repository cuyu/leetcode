#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#

# @lc code=start
from typing import Tuple, List, Set


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == [[]]:
            return False

        height = len(board)
        width = len(board[0])

        def dfs(x: int, y: int, left_word: str, history: Set[Tuple[int, int]]):
            if x < 0 or x >= height or y < 0 or y >= width:
                return False
            if board[x][y] != left_word[0] or (x, y) in history:
                return False
            else:
                if len(left_word) == 1:
                    return True
                else:
                    history_copy = set(history)
                    history_copy.add((x, y))
                    return dfs(x-1, y, left_word[1:], history_copy) \
                        or dfs(x+1, y, left_word[1:], history_copy) \
                        or dfs(x, y-1, left_word[1:], history_copy) \
                        or dfs(x, y+1, left_word[1:], history_copy)

        for i in range(height):
            for j in range(width):
                history = set()
                if dfs(i, j, word, history):
                    return True
        return False
# @lc code=end


if __name__ == "__main__":
    Solution().exist([
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"],
    ], "ABCESEEEFS")
