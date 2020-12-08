from math import ceil, floor


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        tmp = ''
        last_operator = '+'
        for c in s + '+':
            if c not in operators:
                tmp += c
            else:
                number = int(tmp.strip())
                if last_operator == '+':
                    stack.append(number)
                elif last_operator == '-':
                    stack.append(-number)
                elif last_operator == '*':
                    stack[-1] = stack[-1] * number
                else:
                    if stack[-1] >= 0:
                        stack[-1] = floor(stack[-1] / number)
                    else:
                        stack[-1] = ceil(stack[-1] / number)
                last_operator = c
                tmp = ''
        return sum(stack)


if __name__ == "__main__":
    Solution().calculate("14-3/2")
