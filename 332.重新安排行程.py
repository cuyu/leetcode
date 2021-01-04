#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from typing import List


# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = ['JFK']
        used = []

        def dfs(start: str) -> bool:
            if len(used) == len(tickets):
                for i in used:
                    result.append(tickets[i][1])
                return True
            targets = []
            for i, t in enumerate(tickets):
                if i not in used and t[0] == start:
                    targets.append(i)
            # sort by target location name
            tmp = {i: tickets[i][1] for i in targets}
            items = sorted(tmp.items(), key=lambda x: x[1])

            for i, _ in items:
                used.append(i)
                if dfs(tickets[i][1]):
                    return True
                used.remove(i)
            return False

        dfs('JFK')
        return result


# @lc code=end
if __name__ == "__main__":
    Solution().findItinerary(
        [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
