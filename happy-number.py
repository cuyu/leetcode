class Solution:
    def isHappy(self, n: int) -> bool:
        history = {n}
        while 1:
            tmp = 0
            for i in str(n):
                tmp += int(i) ** 2
            if tmp == 1:
                return True
            elif tmp not in history:
                history.add(tmp)
                n = tmp
            else:
                return False
