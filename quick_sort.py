
from typing import List
import random


def partition(nums: List[int], low: int, high: int) -> int:
    number = nums[high]
    j = low
    for i in range(low, high):
        if nums[i] <= number:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    nums[j], nums[high] = nums[high], nums[j]
    return j


def _quick_sort(nums: List[int], low: int, high: int) -> None:
    if low < high:
        p = partition(nums, low, high)
        _quick_sort(nums, low, p-1)
        _quick_sort(nums, p+1, high)


def quick_sort(nums: List[int]):
    _quick_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    a = list(range(10))
    random.shuffle(a)
    quick_sort(a)
    print(a)
