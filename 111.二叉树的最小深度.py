#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            # BFS
            depth = 0
            layer = [root]
            low_layer = []
            found_leaf = False
            while not found_leaf:
                for node in layer:
                    if node.left:
                        low_layer.append(node.left)
                    if node.right:
                        low_layer.append(node.right)
                    elif node.left is None:
                        found_leaf = True
                        break
                depth += 1
                layer = low_layer
                low_layer = []
            return depth

# @lc code=end
