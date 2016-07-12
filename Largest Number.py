"""
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        sorted_nums = sorted(nums, cmp=self.less_than)
        result = ''.join([str(i) for i in sorted_nums])
        # Remove extra zeros at the beginning.
        while result[0] == '0' and len(result) != 1:
            result = result[1:]
        return result

    def less_than(self, a, b):
        a = str(a)
        b = str(b)
        if len(a) < len(b):
            common_length = len(a)
            if int(a) < int(b[:common_length]):
                return 1
            elif int(a) > int(b[:common_length]):
                return -1
            else:
                return self.less_than(a, b[common_length:])
        elif len(a) > len(b):
            common_length = len(b)
            if int(a[:common_length]) < int(b):
                return 1
            elif int(a[:common_length]) > int(b):
                return -1
            else:
                return self.less_than(a[common_length:], b)
        else:
            a, b = int(a), int(b)
            if a < b:
                return 1
            elif a > b:
                return -1
            else:
                return 0


if __name__ == '__main__':
    a = [121, 12]
    print Solution().largestNumber(a)
