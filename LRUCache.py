from typing import Union


class LinkedNode:
    def __init__(self, key: int, value: int) -> None:
        self.value = value
        self.key = key
        self.previous: Union[None, LinkedNode] = None
        self.next: Union[None, LinkedNode] = None


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._mapping = {}
        self._head = None
        self._tail = None

    def get(self, key: int) -> int:
        node = self._mapping.get(key)
        if node is None:
            return -1
        if self._capacity == 1:
            return node.value

        # If is head, move head to next
        if self._head is node:
            self._head = self._head.next
        # Put the node to tail
        p = node.previous
        n = node.next
        if p:
            p.next = n
        if n:
            n.previous = p

        if self._tail is not node:
            self._tail.next = node
            node.previous = self._tail
            node.next = None
        return node.value

    def put(self, key: int, value: int) -> None:
        if self._capacity == 1:
            self._mapping = {key: LinkedNode(key, value)}
        else:
            node = LinkedNode(key, value)
            if self._head is None:
                self._head = node
                self._tail = node
            else:
                if len(self._mapping) >= self._capacity:
                    del self._mapping[self._head.key]
                    self._head = self._head.next
                self._tail.next = node
                node.previous = self._tail
                self._tail = node

            self._mapping[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
