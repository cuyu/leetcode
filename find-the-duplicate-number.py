from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 统计 >2/n 和 <2/n的元素数目，如果元素数目多余n/2则多余元素在那部分中
        left = 0
        right = len(nums)
        while left < right - 1:
            count = 0
            mid = (right - left) // 2 + left
            for n in nums:
                if n <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid
        return right


if __name__ == "__main__":
    Solution().findDuplicate([3, 1, 3, 4, 2])
