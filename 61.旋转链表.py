#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
      if head is None or head.next is None or k <= 0:
        return head
      # Find the new head - the last k node
      fast = head
      count = 0
      while count < k:
        count += 1
        if fast.next != None:
          fast = fast.next
        else:
          # k is larger than link length
          return self.rotateRight(head, k % count)
      slow = head
      while fast.next and slow.next:
        fast = fast.next
        slow = slow.next
      else:
        # fast node is the tail. slow should be the new tail, slow.next should be the new head
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head
        
# @lc code=end

