#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
from typing import List


# @lc code=start
class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.children = []


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        s = str(n)
        depth = len(s)
        # build tree
        root = TreeNode(0)
        layer = [root]
        next_layer = []
        flag = False
        for i in range(depth):
            start = 1 if i == 0 else 0
            for node in layer:
                children = []
                for j in range(start, 10):
                    value = node.val * 10 + j
                    if value <= n:
                        children.append(TreeNode(value))
                    else:
                        flag = True
                        break
                node.children = children
                next_layer += children
                if flag:
                    break
            layer = next_layer
            next_layer = []

        # walk through the tree
        result = []

        def dfs(node: TreeNode):
            if node is None:
                return
            number = node.val
            result.append(number)
            for c in node.children:
                dfs(c)
        dfs(root)
        return result[1:]


# @lc code=end
if __name__ == "__main__":
    Solution().lexicalOrder(13)
