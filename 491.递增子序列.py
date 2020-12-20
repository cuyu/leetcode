#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
from typing import List


# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []
        if len(nums) == 2:
            return [nums] if nums[0] <= nums[1] else []
        result = []
        # subsequence length is 2
        number = nums[0]
        for v in list(set(nums[1:])):
            if v >= number:
                result.append([number, v])
        sequences = self.findSubsequences(nums[1:])
        for s in sequences:
            if s[0] >= number:
                result.append([number, *s])
        for s in sequences:
            if s not in result:
                result.append(s)
        return result
# @lc code=end


if __name__ == "__main__":
    Solution().findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1])
