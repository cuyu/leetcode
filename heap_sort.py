from typing import List


def heapify(tree: List[int], length: int, index: int):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if left_child >= length:
        return
    max_index = index
    if tree[left_child] > tree[max_index]:
        max_index = left_child
    if right_child < length and tree[right_child] > tree[max_index]:
        max_index = right_child
    if max_index != index:
        tmp = tree[index]
        tree[index] = tree[max_index]
        tree[max_index] = tmp
        heapify(tree, length, max_index)


def build_heap(tree: List[int], length: int):
    # 自底向上做heapify
    last_parent = (length - 1 - 1) // 2
    for i in range(last_parent, -1, -1):
        heapify(tree, length, i)


def heap_sort(nums: List[int]) -> None:
    length = len(nums)
    while length > 0:
        build_heap(nums, length)
        # 交换堆顶元素（最大值）和二叉树中位置最后的元素，即摘除堆顶元素后重新进行build_heap，获取第二大的值，以此类推
        tmp = nums[0]
        nums[0] = nums[length - 1]
        nums[length - 1] = tmp
        length -= 1


if __name__ == "__main__":
    # 用数组表示完全二叉树，对于数组中的第i个元素，其：
    # parent = (i - 1) / 2
    # left_child = 2 * i + 1, right_child = 2 * i + 2
    a = [5, 7, 3, 1, 4, 10]
    heap_sort(a)
    print(a)
