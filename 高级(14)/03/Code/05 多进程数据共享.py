import multiprocessing
import threading


def arr_append(arr):
    arr.put(1)
    arr.put(2)
    arr.put(3)
    print('arr:\t', arr)
    print('arr:\t', arr.qsize())


if __name__ == '__main__':
    arr = multiprocessing.Queue(maxsize=10)

    multiprocessing.Process(target=arr_append, args=(arr,)).start()
    multiprocessing.Process(target=arr_append, args=(arr,)).start()
