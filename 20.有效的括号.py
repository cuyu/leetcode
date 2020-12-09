#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            if stack and c in mapping and mapping[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
# @lc code=end


if __name__ == "__main__":
    Solution().isValid("([)]")
