#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#


# @lc code=start
class LinkedNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next: LinkedNode | None = None
        self.prev: LinkedNode | None = None


class LRUCache:
    DEFAULT_VAL = -1

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: dict[int, LinkedNode] = {}
        self._head = LinkedNode(self.DEFAULT_VAL, self.DEFAULT_VAL)
        self._tail = LinkedNode(self.DEFAULT_VAL, self.DEFAULT_VAL)
        self._head.next = self._tail
        self._tail.prev = self._head

    def _move_to_head(self, node: LinkedNode):
        # Move node to the head's next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = self._head.next
        if self._head.next:
            self._head.next.prev = node
        self._head.next = node
        node.prev = self._head

    def get(self, key: int) -> int:
        node = self._cache.get(key)
        if node is None:
            return -1
        else:
            self._move_to_head(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            node = self._cache[key]
            node.val = value
            self._move_to_head(node)
        else:
            # Pop out node before tail
            if len(self._cache) >= self._capacity:
                old_node = self._tail.prev
                if old_node:
                    del self._cache[old_node.key]
                    if old_node.prev:
                        old_node.prev.next = self._tail
                    self._tail.prev = old_node.prev
            # Create a new node and put to head's next
            new_node = LinkedNode(key, value)
            self._move_to_head(new_node)
            self._cache[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
