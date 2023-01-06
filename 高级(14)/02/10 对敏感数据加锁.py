import time
import threading
import random

# 1. 创建一把锁
lock = threading.Lock()
num = 0


def add():
    global num
    for i in range(1000000):
        # 2. 获取一把锁
        lock.acquire()
        num += 1
        # 3. 释放一把锁
        lock.release()

    print('add:\t', num)  # 最终的结果是对的


if __name__ == '__main__':
    # add()
    # add()
    threading.Thread(target=add).start()
    threading.Thread(target=add).start()

"""
    加了锁之后两个线程的执行顺序是不一样的,不知道第一个线程是怎么执行的,但知道最终的结果是正确的
    加锁保护最后的结果是正确的
"""
