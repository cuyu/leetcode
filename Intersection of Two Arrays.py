"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        # Remove duplicates.
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums1.sort()
        nums2.sort()
        index = 0
        for i in nums1:
            while index < len(nums2) and i >= nums2[index]:
                if i == nums2[index]:
                    result.append(i)
                index += 1
        return result


if __name__ == '__main__':
    print Solution().intersection([1, 2, 2, 1], [2, 2])
