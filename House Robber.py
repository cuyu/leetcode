"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            # Just pick the first house is good enough
            if nums[0] >= nums[1]:
                return nums[0] + self.rob(nums[2:])
            # The second house is a must pick
            elif nums[1] > nums[0] + nums[2]:
                return nums[1] + self.rob(nums[3:])
            else:
                return max(nums[0] + self.rob(nums[2:]), nums[1] + self.rob(nums[3:]))


class OtherSolution:
    def rob(self, nums: List[int]) -> int:
        # Record the total money of two different choices (i.e. we cache the result of previous choice)
        amount = [0, 0]
        for money in nums:
            # For amount[-2], it must not contain the money of previous house, but for amount[-1] it may contain the
            # money of previous house (or may not, in this condition, amount[-2] == amount[-1]),
            # so we store the better result of:
            # 1. rob current house, but without previous house
            # 2. rob previous house without current house
            # ---
            # DP[n] = max(DP[n-1], DP[n-2] + nums[-1])
            # DP[0] = 0, DP[1] = DP[2] = max(nums)
            amount.append(max(amount[-1], amount[-2] + money))
        return amount[-1]


if __name__ == '__main__':
    print(OtherSolution().rob([2, 1, 1, 2]))
