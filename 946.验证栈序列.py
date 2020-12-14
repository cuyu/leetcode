#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#
from typing import List


# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0
        while j < len(popped):
            while 1:
                if stack and stack[-1] == popped[j]:
                    stack.pop()
                    j += 1
                else:
                    break
            if i == len(pushed) == j:
                return True
            while (not stack) or stack[-1] != popped[j]:
                if i >= len(pushed):
                    return False
                stack.append(pushed[i])
                i += 1

        return not stack
# @lc code=end


if __name__ == "__main__":
    Solution().validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
