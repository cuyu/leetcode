from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._segment_tree = [0] * 2 * len(nums)
        # 线段树的索引i对应了范围从2^(i-n)
        for i in range(len(nums)):
            self._segment_tree[i + len(nums)] = nums[i]
        for i in range(len(nums) - 1, 0, -1):
            self._segment_tree[i] = self._segment_tree[i *
                                                       2] + self._segment_tree[i * 2 + 1]

    def update(self, i: int, val: int) -> None:
        k = i + len(self._nums)
        diff = val - self._segment_tree[k]
        while k > 0:
            self._segment_tree[k] += diff
            k //= 2

    def sumRange(self, i: int, j: int) -> int:
        result = 0
        l = len(self._nums) + i
        r = len(self._nums) + j
        while l <= r:
            if l % 2 == 1:
                result += self._segment_tree[int(l)]
                l += 1
            if r % 2 == 0:
                result += self._segment_tree[int(r)]
                r -= 1
            l //= 2
            r //= 2
        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


if __name__ == "__main__":
    a = NumArray([1, 3, 5, 7, 2, 4])
    a.update(1, 2)
    print(a.sumRange(1, 3))
