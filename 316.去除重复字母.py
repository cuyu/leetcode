#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
from collections import defaultdict


# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return s
        remain = defaultdict(int)
        for c in s:
            remain[c] += 1
        result = []
        for c in s:
            if c not in result:
                while result and c < result[-1] and remain[result[-1]] > 0:
                    result.pop()
                result.append(c)
            remain[c] -= 1
        return ''.join(result)

# @lc code=end


if __name__ == "__main__":
    Solution().removeDuplicateLetters("bcabc")
