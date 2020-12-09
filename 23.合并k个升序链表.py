#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list_nodes(nums: List[int]) -> ListNode:
    head = ListNode(nums[0])
    h = head
    for n in nums[1:]:
        h.next = ListNode(n)
        h = h.next
    return head


# @lc code=start
def heapify(lists: List[ListNode], i: int):
    left_child = i * 2 + 1
    right_child = i * 2 + 2
    min_index = i
    if left_child < len(lists) and lists[min_index].val > lists[left_child].val:
        min_index = left_child
    if right_child < len(lists) and lists[min_index].val > lists[right_child].val:
        min_index = right_child
    if min_index != i:
        tmp = lists[i]
        lists[i] = lists[min_index]
        lists[min_index] = tmp
        heapify(lists, min_index)


def build_heap(lists: List[ListNode]):
    i = (len(lists) - 1) // 2
    while i >= 0:
        heapify(lists, i)
        i -= 1


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = None
        # Remove empty list node
        new_lists = []
        for i in range(len(lists)):
            if lists[i]:
                new_lists.append(lists[i])
        lists = new_lists
        build_heap(lists)
        while lists:
            h = lists[0]
            if head is None:
                head = h
                tmp = head
            else:
                tmp.next = h
                tmp = tmp.next
            h = h.next
            lists[0] = h
            if h:
                heapify(lists, 0)
            else:
                lists[0] = lists[-1]
                del lists[-1]
                heapify(lists, 0)
        return head
# @lc code=end


if __name__ == "__main__":
    lists = [
        build_list_nodes([-1, 1]),
        build_list_nodes([-3, 1, 4]),
        build_list_nodes([-2, -1, 0, 2]),
    ]
    Solution().mergeKLists(lists)
