#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        n = str(num)
        s = [x for x in n]

        last = {}
        for i, c in enumerate(s):
            last[c] = i
        for i, c in enumerate(s):
            for j in range(9, int(c), -1):
                x = str(j)
                if x in last and last[x] > i:
                    s[i], s[last[x]] = s[last[x]], s[i]
                    return int(''.join(s))
        return num
# @lc code=end


if __name__ == "__main__":
    Solution().maximumSwap(10)
