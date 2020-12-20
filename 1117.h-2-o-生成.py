#
# @lc app=leetcode.cn id=1117 lang=python3
#
# [1117] H2O 生成
#
import threading


def releaseHydrogen():
    print('H')


def releaseOxygen():
    print('O')


# @lc code=start

INDEX = 1


class H2O:
    def __init__(self):
        self._locks = [threading.Lock() for _ in range(3)]
        self._locks[0].acquire()

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        global INDEX

        with self._locks[0]:
            # releaseHydrogen() outputs "H". Do not change or remove this line.
            releaseHydrogen()
            self._locks[INDEX].release()
            INDEX += 1
        if INDEX > 2:
            INDEX = 1
            self._locks[0].acquire()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self._locks[1]:
            with self._locks[2]:
                # releaseOxygen() outputs "O". Do not change or remove this line.
                releaseOxygen()
                self._locks[0].release()
        self._locks[1].acquire()
        self._locks[2].acquire()

# @lc code=end


if __name__ == "__main__":
    from threading import Thread

    F = H2O()
    t1 = threading.Thread(target=F.hydrogen, args=(releaseHydrogen,))
    t2 = threading.Thread(target=F.hydrogen, args=(releaseHydrogen,))
    t3 = threading.Thread(target=F.oxygen, args=(releaseOxygen,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
