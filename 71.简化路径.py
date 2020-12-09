#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split('/'):
            if i in {'.', ''}:
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return '/' + '/'.join(stack)
# @lc code=end


if __name__ == "__main__":
    Solution().simplifyPath("/a/../../b/../c//.//")
