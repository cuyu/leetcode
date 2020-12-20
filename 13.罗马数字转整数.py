#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
DICT = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
SPECIAL_DICT = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        if s in DICT:
            return DICT[s]
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in SPECIAL_DICT:
                result += SPECIAL_DICT[s[i:i+2]]
                i += 2
            else:
                result += DICT[s[i]]
                i += 1
        return result

# @lc code=end


if __name__ == "__main__":
    Solution().romanToInt("MCMXCIV")
