#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#
from typing import List


# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        set1 = set()
        set2 = set()
        history = set()

        def dfs(source: int, targets: List[int]) -> bool:
            history.add(source)
            if source in set1:
                for j in targets:
                    if j in set1:
                        return False
                    set2.add(j)
            if source in set2:
                for j in targets:
                    if j in set2:
                        return False
                    set1.add(j)
            for t in targets:
                if t in history:
                    continue
                if not dfs(t, graph[t]):
                    return False
            return True
        while len(history) != len(graph):
            # pick one edge
            for i in range(len(graph)):
                if i not in history:
                    targets = graph[i]
                    set1.add(i)
                    for j in targets:
                        if j == i:
                            return False
                        set2.add(j)
                    if not dfs(i, targets):
                        return False
        return True
# @lc code=end


if __name__ == "__main__":
    Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
