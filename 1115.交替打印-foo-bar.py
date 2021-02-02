#
# @lc app=leetcode.cn id=1115 lang=python3
#
# [1115] 交替打印FooBar
#
# @lc code=start
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.lock_foo = threading.Lock()
        self.lock_bar = threading.Lock()
        self.lock_bar.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_foo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.lock_bar.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.lock_bar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock_foo.release()
# @lc code=end


if __name__ == '__main__':
    def printFoo():
        print('foo')

    def printBar():
        print('bar')

    foobar = FooBar(2)
    t1 = threading.Thread(target=foobar.foo, args=(printFoo,))
    t2 = threading.Thread(target=foobar.bar, args=(printBar,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
