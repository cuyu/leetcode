#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
from collections import deque


# @lc code=start
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._in_queue = deque()
        self._out_queue = deque()
        self._top_in = True

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self._top_in:
            self._in_queue.append(x)
            while len(self._in_queue) != 1:
                self._out_queue.append(self._in_queue.popleft())
        else:
            self._out_queue.append(x)
            while len(self._out_queue) != 1:
                self._in_queue.append(self._out_queue.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self._top_in:
            r = self._in_queue.popleft()
            if len(self._out_queue) > 0:
                while len(self._out_queue) != 1:
                    self._in_queue.append(self._out_queue.popleft())
        else:
            r = self._out_queue.popleft()
            if len(self._in_queue) > 0:
                while len(self._in_queue) != 1:
                    self._out_queue.append(self._in_queue.popleft())
        self._top_in = not self._top_in
        return r

    def top(self) -> int:
        """
        Get the top element.
        """
        if self._top_in:
            return self._in_queue[0]
        else:
            return self._out_queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._in_queue) == 0 and len(self._out_queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.pop()
    s.pop()
