#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#


# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res = ""
        tmp = abs(num)
        while tmp > 0:
            left = tmp % 7
            res = str(left) + res
            tmp = tmp // 7
        res = "-" + res if num < 0 else res
        return res


# @lc code=end
if __name__ == "__main__":
    Solution().convertToBase7(-7)
