#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# TODO: failed
# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        lower = 0
        upper = len(nums)
        res = (upper - lower) // 2
        flag = 0
        while 1:
            if target > nums[res]:
                lower = res
                flag = 1
            elif target < nums[res]:
                upper = res
                flag = -1
            else:
                return res
            res_new = (upper - lower) // 2
            if res_new == res:
                return res + flag
            res = res_new
        return -1


# @lc code=end
if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 7], 4))
