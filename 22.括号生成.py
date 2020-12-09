#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        if n == 1:
            return ['()']
        possibies = self.generateParenthesis(n - 1)
        result = []
        for p in possibies:
            r = []
            # Insert ')' after next '(', vice visa
            tmp = '(' + p
            for i in range(len(tmp)):
                if tmp[i] == '(':
                    r.append(tmp[:i+1] + ')' + tmp[i+1:])
            result += r
        return list(set(result))
# @lc code=end


if __name__ == "__main__":
    Solution().generateParenthesis(3)
