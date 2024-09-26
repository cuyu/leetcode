#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      res: List[List[int]] = []
      if root is None:
        return res
      current_level_nodes: List[TreeNode] = [root]
      next_level_nodes: List[TreeNode] = []
      while current_level_nodes:
        tmp: List[int] = []
        for node in current_level_nodes:
          tmp.append(node.val)
          if node.left:
            next_level_nodes.append(node.left)
          if node.right:
            next_level_nodes.append(node.right)
        res.append(tmp)
        current_level_nodes = next_level_nodes
        next_level_nodes = []
      return res
      
# @lc code=end

