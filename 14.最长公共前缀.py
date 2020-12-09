#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for s in strs[1:]:
            tmp = ''
            for i in range(min(len(s), len(prefix))):
                if prefix[i] == s[i]:
                    tmp += s[i]
                else:
                    break
            prefix = tmp
        return prefix
# @lc code=end


if __name__ == "__main__":
    Solution().longestCommonPrefix(["flower", "flow", "flight"])
