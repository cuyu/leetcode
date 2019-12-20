"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
from typing import List


class Solution:
    def previous_rob(self, nums: List[int]) -> int:
        amount = [0, 0]
        for money in nums:
            amount.append(max(amount[-1], amount[-2] + money))
        return amount[-1]

    def rob(self, nums: List[int]) -> int:
        # Using DP[i, j] to describe house range from i to j-1, DP1 is the solution of House Robber.py
        # DP2[0, n] = max(DP1[1, n-2] + nums[-1], DP1[2, n-1] + nums[0], DP1[1, n-1])
        if len(nums) < 4:
            nums.append(0)
            return max(nums)
        return max(self.previous_rob(nums[1:-2]) + nums[-1], self.previous_rob(nums[2:-1]) + nums[0],
                   self.previous_rob(nums[1:-1]))


if __name__ == '__main__':
    print(Solution().rob([2, 7, 7, 7, 4]))
