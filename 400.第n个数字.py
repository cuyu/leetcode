#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        n_digit = 1
        tmp = n - 10
        if tmp < 0:
            return n
        left = tmp
        while tmp >= 0:
            left = tmp
            tmp -= (n_digit + 1) * 9 * (10 ** n_digit)
            n_digit += 1
        number = 10 ** (n_digit - 1) + left // n_digit
        result = str(number)[left % n_digit]
        return int(result)
# @lc code=end


if __name__ == "__main__":
    Solution().findNthDigit(10)
