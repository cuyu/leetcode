from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for i in nums:
            current_length = 1
            # 等到遍历到i-1时再进行计算长度，避免重复计算
            if (i - 1) not in nums_set:
                i += 1
                while i in nums_set:
                    current_length += 1
                    i += 1
                if current_length > max_length:
                    max_length = current_length
        return max_length


if __name__ == "__main__":
    Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
