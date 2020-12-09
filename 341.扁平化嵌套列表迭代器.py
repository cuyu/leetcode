#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

def flattern(nestedList: [NestedInteger]) -> List[int]:
    flat = []
    stack = []
    indexes = []
    index = 0
    layer = nestedList
    while 1:
        if index < len(layer):
            tmp = layer[index]
            if tmp.isInteger():
                index += 1
                flat.append(tmp.getInteger())
            else:
                stack.append(layer)
                index += 1
                indexes.append(index)
                layer = tmp.getList()
                index = 0
        else:
            if stack:
                layer = stack.pop()
                index = indexes.pop()
            else:
                break
    return flat


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._flat = flattern(nestedList)
        self._index = 0

    def next(self) -> int:
        r = self._flat[self._index]
        self._index += 1
        return r

    def hasNext(self) -> bool:
        return self._index < len(self._flat)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
