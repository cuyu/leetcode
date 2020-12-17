#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
from typing import List, Tuple


# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s: str, s_index: int, ip_index: int) -> Tuple[bool, List[str]]:
            if ip_index == 4 and s_index == len(s):
                return True, ['']
            elif ip_index == 4 or s_index == len(s):
                return False, []
            addresses = []
            if s[s_index] == '0':
                end = s_index + 1
                is_valid, left = dfs(s, end, ip_index + 1)
                if is_valid:
                    for l in left:
                        addresses.append('0.' + l)
                else:
                    return False, []
            else:
                for i in range(3):
                    end = s_index + i + 1
                    if end <= len(s):
                        num = s[s_index:end]
                        if 0 <= int(num) <= 255:
                            is_valid, left = dfs(s, end, ip_index + 1)
                            if is_valid:
                                for l in left:
                                    addresses.append(num + '.' + l)
            return True, addresses

        _, result = dfs(s, 0, 0)
        return [r[:-1] for r in result]
# @lc code=end


if __name__ == "__main__":
    Solution().restoreIpAddresses("25525511135")
