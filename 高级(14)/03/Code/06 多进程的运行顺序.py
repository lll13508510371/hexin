import multiprocessing
import threading
import time


def work(name):
    for i in range(10):
        print(f'{name} {i}工作中...')
        time.sleep(0.4)


if __name__ == '__main__':
    # daemon 设置进程为守护进程,当主进程挂掉之后,子进程就也跟着挂掉

    multiprocessing.Process(target=work, args=('p1', ), daemon=True).start()
    p2 = multiprocessing.Process(target=work, args=('p2', ))
    p2.daemon = True
    p2.start()
    time.sleep(2)
    print('主进程执行完毕了')
