from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p1_end = m
        p2 = 0
        while p2 < len(nums2) and p1 < p1_end:
            n = nums2[p2]
            if n < nums1[p1]:
                nums1.insert(p1, n)
                del nums1[-1]
                p1 += 1
                p2 += 1
                p1_end += 1
            else:
                p1 += 1
        if p2 < len(nums2):
            for i in nums2[p2:]:
                nums1[p1] = i
                p1 += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    Solution().merge(nums1, 3, [2, 5, 6], 3)
    print(nums1)
