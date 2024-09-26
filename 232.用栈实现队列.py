#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
      self._stack_in = []
      self._stack_out = []

    def push(self, x: int) -> None:
      self._stack_in.append(x)

    def _prepare(self):
      if len(self._stack_out) == 0:
        while len(self._stack_in) > 0:
          tmp = self._stack_in.pop()
          self._stack_out.append(tmp)

    def pop(self) -> int:
      self._prepare()
      return self._stack_out.pop()

    def peek(self) -> int:
      self._prepare()
      return self._stack_out[-1]

    def empty(self) -> bool:
      return len(self._stack_in) == 0 and len(self._stack_out) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

