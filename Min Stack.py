"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._elements = []
        self._min_index = 0
        # The last element is the latest min index
        self._min_index_history = [0]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._elements.append(x)
        if self._elements[self._min_index] > x:
            self._min_index = len(self._elements) - 1
            self._min_index_history.append(self._min_index)

    def pop(self):
        """
        :rtype: void
        """
        if self._min_index == len(self._elements) - 1 and len(self._elements) > 1:
            self._min_index_history.pop()
            self._min_index = self._min_index_history[-1]
        return self._elements.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._elements[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._elements[self._min_index]


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
