#
# @lc app=leetcode.cn id=670 lang=python3
#
# [670] 最大交换
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        n = str(num)
        s = [x for x in n]
        low = 0
        high = len(s) - 1
        replaced = -1
        while low < len(s):
            if low >= high:
                if replaced != -1:
                    break
                low += 1
                high = len(s) - 1
            else:
                if s[low] < s[high]:
                    if replaced == -1:
                        s[low], s[high] = s[high], s[low]
                    else:
                        # 如果找到了更大的数，则先把之前交换的复原，再以新的更大的数做交换
                        s[low], s[replaced] = s[replaced], s[low]
                        s[low], s[high] = s[high], s[low]
                    replaced = high
                high -= 1
        return int(''.join(s))

# @lc code=end


if __name__ == "__main__":
    Solution().maximumSwap(120)
