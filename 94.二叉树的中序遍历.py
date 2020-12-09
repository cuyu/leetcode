#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        if root.left is None:
            return [root.val] + self.inorderTraversal(root.right)
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# @lc code=end
