import multiprocessing
import threading
import concurrent.futures
import time

urls = ['http://www.baidu.com?page={}'.format(page) for page in range(1, 100)]


def download(url):
    print(url)
    time.sleep(1)


# 100 个任务 --> 100s
# 10 个线程  --> 10s
# 10 个进程  --> 10s
# 10 个进程 + 10 个线程 --> 1s
# cpu 核心数*2+1个进程,每个进程开两个线程 web服务

def thread_poll_download(url2):
    executor2 = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    # for url2 in urls2:
        # download(url)
    """直接用线程很容易造成内存溢出,因为同时执行很多的任务"""
        # threading.Thread(target=download, args=(url,)).start()
        # 往池子里面分派(丢)任务
    executor2.submit(download, url2)


if __name__ == '__main__':
    # 多线程并发池
    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    # 多进程并发池
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=10)
    # for i in range(10, 101, 10):  # --> 10 20 30 40 50 60 70 80 90 100
        # download(url)
        # print(urls[i - 10:i])
    for url in urls:
        executor.submit(thread_poll_download, url)
    """直接用线程很容易造成内存溢出"""
    # executor.submit(thread_poll_download, urls)

    print('主线程运行完毕')

'''
!!!
for url in urls:
    threading.Thread(target=download, arg=(url,))
这样就会循环一次就开一个线程,如果爬虫的话,可能一次就爬一百万个数据,这样会开一百万个线程,直接就卡住了
'''
'''
请求数据 --> time.sleep()(等待服务器将请求数据发回) -->得到数据
'''
