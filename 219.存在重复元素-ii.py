#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        group = set(nums[: k + 1])
        if len(group) < len(nums[: k + 1]):
            return True
        for i in range(k + 1, len(nums)):
            group.remove(nums[i - k - 1])
            if nums[i] in group:
                return True
            else:
                group.add(nums[i])
        return False


# @lc code=end
if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
