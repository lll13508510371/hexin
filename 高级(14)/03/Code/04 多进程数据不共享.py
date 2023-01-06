import multiprocessing
import threading
import time


def arr_append(arr):
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print('arr:\t', arr)


if __name__ == '__main__':
    # arr = []
    # arr_append(arr)
    # arr_append(arr)
    arr = []
    threading.Thread(target=arr_append, args=(arr,)).start()
    threading.Thread(target=arr_append, args=(arr,)).start()
    time.sleep(2)
    arr = []
    multiprocessing.Process(target=arr_append, args=(arr,)).start()
    multiprocessing.Process(target=arr_append, args=(arr,)).start()

    """
        多线程数据共享,会引发线程竞争问题,导致敏感数据出错,加锁可以保证敏感数据没有问题
        
        多进程数据不共享,会出现数据无法同步,会出现进程之间无法数据交换,使用进程之间的对垒可以解决
        进程间数据交换问题
    """

    '''
        https://www.cnblogs.com/purple5252/p/12957544.html
        并行：当系统有一个以上CPU时,则线程的操作有可能非并发。当一个CPU执行一个线程时，另一个CPU可以执行另一个线程，两个线程互不抢占CPU资源，可以同时进行，这种方式我们称之为并行(Parallel)
        ---->   当系统有一个以上CPU时,则线程的操作有可能非并发  这句话表明当有一个以上核心时,线程操作可能是并行也可能是并发
        ---->   我的CPU内核是8,但在这里运行线程的时候还是并发(一个核来处理)
                arr:	 [1, 2, 3]
                arr:	 [1, 2, 3, 1, 2, 3]
    '''
