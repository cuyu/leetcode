class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        # 表示以第i个元素开头的最长子串长度
        length = [0] * (len(s) + 1)
        substring = set()
        while r < len(s):
            i = r
            while i < len(s) and s[i] not in substring:
                substring.add(s[i])
                length[l] += 1
                i += 1
            r = i
            l += 1
            substring.remove(s[l - 1])
            length[l] = length[l - 1] - 1
        return max(length)


if __name__ == "__main__":
    Solution().lengthOfLongestSubstring("abababa")
