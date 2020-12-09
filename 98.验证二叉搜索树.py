#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self._isValid(root, float('-inf'), float('inf'))

    def _isValid(self, root: TreeNode, limit_low: float, limit_high: float) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if root.val <= root.left.val or (not (limit_low < root.left.val < limit_high)):
                return False
        if root.right is not None:
            if root.val >= root.right.val or (not (limit_low < root.right.val < limit_high)):
                return False
        return self._isValid(root.left, limit_low, root.val) and self._isValid(root.right, root.val, limit_high)
# @lc code=end
