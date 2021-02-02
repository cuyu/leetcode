#
# @lc app=leetcode.cn id=1116 lang=python3
#
# [1116] 打印零与奇偶数
#

# @lc code=start
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock0 = threading.Lock()
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()

        # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.lock0.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.lock1.release()
            else:
                self.lock2.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n // 2):
            self.lock2.acquire()
            printNumber(2 * (i + 1))
            self.lock0.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n + 1) // 2):
            self.lock1.acquire()
            printNumber(2 * i + 1)
            self.lock0.release()


# @lc code=end
if __name__ == "__main__":
    z = ZeroEvenOdd(5)
    t1 = threading.Thread(target=z.zero, args=(print,))
    t2 = threading.Thread(target=z.odd, args=(print,))
    t3 = threading.Thread(target=z.even, args=(print,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
