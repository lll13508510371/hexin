import multiprocessing
import threading
import time


def download():
    print('开始下载文件...')
    time.sleep(1)
    print('完成下载文件')


def upload():
    print('开始上传文件...')
    time.sleep(1)
    print('完成上传文件')


# download()
# upload()
# threading.Thread(target=download).start()
# threading.Thread(target=upload).start()
if __name__ == '__main__':
    ''' 多进程一定要运行在 if __name__ == '__main__' 下面'''
    multiprocessing.Process(target=download).start()
    multiprocessing.Process(target=upload).start()
