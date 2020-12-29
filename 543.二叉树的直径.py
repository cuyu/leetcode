#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @lc code=start
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameterByNode(n: TreeNode):
            def dfs(node: TreeNode) -> int:
                if node is None:
                    return 0
                l = dfs(node.left)
                r = dfs(node.right)
                return 1 + max(l, r)

            if n is None:
                return 0
            l = dfs(n.left)
            r = dfs(n.right)
            return l + r
        if root is None:
            return 0
        diameter = 0
        layer = [root]
        next_layer = []
        while layer:
            for n in layer:
                d = diameterByNode(n)
                if d > diameter:
                    diameter = d
                if n.left:
                    next_layer.append(n.left)
                if n.right:
                    next_layer.append(n.right)
            layer = next_layer
            next_layer = []
        return diameter
# @lc code=end
