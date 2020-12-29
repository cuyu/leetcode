#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class LinkedNode:
    def __init__(self, key, val, next=None) -> None:
        self.val = val
        self.key = key
        self.next = next


BIN_COUNT = 763


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = [None] * BIN_COUNT

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % BIN_COUNT
        if self.mapping[index] is None:
            self.mapping[index] = LinkedNode(key, value)
        else:
            head = self.mapping[index]
            if head.key == key:
                head.val = value
            else:
                if head.next:
                    p = head.next
                    while p and p.key != key:
                        p = p.next
                        head = head.next
                    if p is None:
                        head.next = LinkedNode(key, value)
                    else:
                        p.val = value
                else:
                    head.next = LinkedNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % BIN_COUNT
        if self.mapping[index]:
            head = self.mapping[index]
            while head and head.key != key:
                head = head.next
            return head.val if head else -1
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % BIN_COUNT
        if self.mapping[index]:
            head = self.mapping[index]
            if head.key == key:
                self.mapping[index] = head.next
            else:
                p = head.next
                while p and p.key != key:
                    head = head.next
                    p = p.next
                if p:
                    head.next = p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

if __name__ == "__main__":
    m = MyHashMap()
    m.put(1, 1)
    m.put(2, 2)
    m.get(1)
    m.get(3)
    m.put(2, 1)
