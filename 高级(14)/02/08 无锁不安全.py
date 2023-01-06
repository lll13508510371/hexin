import time
import threading
import random

num = 0


def add():
    global num
    for i in range(1000000):
        num += 1
    print('add:\t', num)


if __name__ == '__main__':
    # add()
    # add()
    threading.Thread(target=add).start()
    threading.Thread(target=add).start()

"""
    两个人同时修改一篇论文,最终进行保存的之后,肯定会有一个人的会被覆盖
e.g.    add:	 1085969
        add:	 1000000
多线程会共用全局变量num,造成数据错乱

"""
