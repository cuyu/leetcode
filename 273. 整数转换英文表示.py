from typing import List


DICT = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety',
    100: 'Hundred',
    1000: 'Thousand',
    1000000: 'Million',
    1000000000: 'Billion',
}
DIRECT_MAPPING = {k: v for k, v in DICT.items() if k < 100}
TY_MAPPING = {k: v for k, v in DICT.items() if 19 < k < 100}
UNITS = [k for k in DICT.keys() if k >= 100][::-1]


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        else:
            return ' '.join(self._numberToWords(num))

    def _numberToWords(self, num: int) -> List[str]:
        if num == 0:
            return []
        if num in DIRECT_MAPPING:
            return [DIRECT_MAPPING[num]]

        result = []
        for unit in UNITS:
            if num >= unit:
                result += [*self._numberToWords(num // unit), DICT[unit]]
                num -= (num // unit) * unit
        if num > 19:
            tmp = (num // 10) * 10
            result += [DICT[tmp], *self._numberToWords(num - tmp)]
        else:
            result += self._numberToWords(num)
        return result


if __name__ == "__main__":
    Solution().numberToWords(1234567)
