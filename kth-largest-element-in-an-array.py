from typing import List


def heapify(tree: List[int], length: int, index: int):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if left_child >= length:
        return
    min_index = index
    if tree[left_child] < tree[min_index]:
        min_index = left_child
    if right_child < length and tree[right_child] < tree[min_index]:
        min_index = right_child
    if min_index != index:
        tmp = tree[index]
        tree[index] = tree[min_index]
        tree[min_index] = tmp
        heapify(tree, length, min_index)


def build_heap(tree: List[int], length: int):
    # 自底向上做heapify
    last_parent = (length - 1 - 1) // 2
    for i in range(last_parent, -1, -1):
        heapify(tree, length, i)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 先创建k个元素的小顶堆，再比较剩下的元素和堆顶，如果更大，则替换堆顶并重新heapify
        tree = list(nums[:k])
        build_heap(tree, k)
        for n in nums[k:]:
            if n > tree[0]:
                tree[0] = n
                heapify(tree, k, 0)
        return tree[0]
