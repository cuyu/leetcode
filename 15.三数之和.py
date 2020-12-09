#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            target = -nums[i]
            # Avoid repeat compute
            if i > 1 and nums[i - 1] == nums[i]:
                continue
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                tmp = nums[lp] + nums[rp]
                if tmp == target:
                    result.append((nums[i], nums[lp], nums[rp]))
                    lp += 1
                    rp -= 1
                elif tmp < target:
                    lp += 1
                else:
                    rp -= 1
        # Remove deplicates
        r = []
        for l in set(result):
            r.append(list(l))
        return r
# @lc code=end


if __name__ == "__main__":
    Solution().threeSum([-1, 0, 1, 2, -1, -4])
