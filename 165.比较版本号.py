#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        while len(v1) < len(v2):
            v1.append('0')
        while len(v2) < len(v1):
            v2.append('0')
        for s1, s2 in zip(v1, v2):
            n1 = int(s1)
            n2 = int(s2)
            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1
        return 0
# @lc code=end
