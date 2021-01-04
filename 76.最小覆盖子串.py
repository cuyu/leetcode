#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
from collections import Counter


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(c1: Counter, c2: Counter) -> bool:
            for k in c2:
                if c1[k] < c2[k]:
                    return False
            return True

        target = Counter(t)
        window = Counter('')
        i = 0
        j = 1
        while s[i] not in target:
            i += 1
            j += 1
            if i >= len(s):
                return ''
        else:
            window[s[i]] += 1

        result = ''
        flag = True
        while 1:
            if flag:
                if i >= len(s):
                    return result
                while i < len(s) and s[i] not in target:
                    i += 1
                else:
                    flag = False

            if is_valid(window, target):
                if result == '' or len(result) > (j - i):
                    result = s[i:j]
                flag = True
                window[s[i]] -= 1
                i += 1
            else:
                if j >= len(s):
                    return result
                if s[j] in target:
                    window[s[j]] += 1
                j += 1
        return result


# @lc code=end
if __name__ == "__main__":
    Solution().minWindow("ab", "a")
