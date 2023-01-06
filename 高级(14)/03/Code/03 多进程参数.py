import multiprocessing
import threading
import time


def run_process(*args, **kwargs):
    print('args:\t', args)
    print('kwargs:\t', kwargs)


if __name__ == '__main__':
    multiprocessing.Process(target=run_process,
                            args=(1, 2, 3, 4),
                            kwargs={'a': 1, 'b': '2'}).start()
