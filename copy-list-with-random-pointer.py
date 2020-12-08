
class Node:
    def __init__(self, x: int, random: 'Node' = None, next: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        new_head = Node(head.val)
        h2 = new_head
        h1 = head
        length = 1
        while h1.next:
            h1 = h1.next
            node = Node(h1.val)
            h2.next = node
            h2 = h2.next
            length += 1
        # Copy random
        h1 = head
        h2 = new_head
        while h1:
            count1 = 0
            count2 = length
            cur = h1.random
            if cur is not None:
                while cur:
                    cur = cur.next
                    count1 += 1
                cur = new_head
                while cur:
                    if count2 == count1:
                        h2.random = cur
                        break
                    cur = cur.next
                    count2 -= 1

            h1 = h1.next
            h2 = h2.next

        return new_head


if __name__ == "__main__":
    node0 = Node(7, None)
    node1 = Node(13, node0)
    node2 = Node(11)
    node3 = Node(10, node2)
    node4 = Node(1, node0)
    node2.random = node4
    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    head = node0
    copy_head = Solution().copyRandomList(head)
    head.next.val = -1
    head.next.next.random.val = -2
    assert copy_head.next.val == 13
    assert copy_head.next.next.random.val == 1
