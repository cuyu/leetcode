"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in
range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches
required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""
from typing import List


class SolutionV1:
    """
    Find the sum combinations, and insert the missing ones, e.g., for nums = [1, 5, 10], n = 20:
    the sum combination is: {1,5,6,10,11,15,16}
    '2' is missing, so add '2'
    => {1,2,3,5,6,7,10,11,12,13,15,16,17,18}
    '4' is missing, add '4' and so on
    """
    def minPatches(self, nums: List[int], n: int) -> int:
        if not nums:
            nums = [1]
            num_patch = 1
        else:
            num_patch = 0
        sums = self.cal_combination_sum(nums)
        for i in range(1, n + 1):
            if i not in sums:
                num_patch += 1
                sums = self._update_combination_sum(i, sums)

        return num_patch

    def cal_combination_sum(self, nums):
        """
        Give a list of numbers, return the sum of all combinations.
        """
        if len(nums) == 1:
            return set(nums)
        i = nums[0]
        exist_sums = self.cal_combination_sum(nums[1:])
        result = self._update_combination_sum(i, exist_sums)

        return result

    def _update_combination_sum(self, new_number, exist_sums):
        result = set(exist_sums)
        if new_number not in exist_sums:
            result.add(new_number)
        for sum in exist_sums:
            tmp = new_number + sum
            if tmp not in exist_sums:
                result.add(tmp)
        return result


class SolutionV2:
    """
    Based on V1, for nums = [1, 5, 10], n = 30, assume we have found the result of nums = [1, 5, 10], n = 22, and the
    patch number is [2, 4], then we add/patch '23', we will get the sum range 1 ~ 22+23=45,i.e. the sum range is doubled
    and plus one, the problem becomes we need to find the minimal sum range which can cover range(1, n)
    """
    def minPatches(self, nums: List[int], n: int) -> int:
        pass


if __name__ == '__main__':
    print(SolutionV1().minPatches([1, 2, 31, 33], 2147483647))
