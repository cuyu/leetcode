#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class UglyNumber:
    number = []

    def __init__(self) -> None:
        if not self.number:
            numbers = [1]
            limit = 1690
            p_list = [0, 0, 0]
            while len(numbers) < limit:
                r2 = numbers[p_list[0]] * 2
                r3 = numbers[p_list[1]] * 3
                r5 = numbers[p_list[2]] * 5
                min_num = min(r2, r3, r5)
                for i, v in enumerate([r2, r3, r5]):
                    if v == min_num:
                        p_list[i] += 1
                numbers.append(min_num)
            self.number = numbers


class Solution:
    u = UglyNumber()

    def nthUglyNumber(self, n: int) -> int:
        return self.u.number[n - 1]
# @lc code=end


if __name__ == "__main__":
    Solution().nthUglyNumber(10)
