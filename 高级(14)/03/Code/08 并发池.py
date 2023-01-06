import multiprocessing
import threading
import concurrent.futures
import time

urls = ['http://www.baidu.com?page={}'.format(page) for page in range(1, 100)]


def download(url):
    # 线程处理等待任务(请求url)会更快
    time.sleep(0.5)
    print(url)
    # 进程处理算数更快
    # total = 0
    # for i in range(1000000):
    #     total += i


if __name__ == '__main__':

    # 多线程并发池
    # executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
    # 多进程并发池
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(download, url)
    print('线程池运行时间:\t', time.time() - start_time)
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(download, url)
    print('进程池运行时间:\t', time.time() - start_time)
    print('主线程运行完毕')

"""
    请求一千个url,多线程比多进程的运行速度更快
    直接运行加法运算,多进程的速度比多线程更快
    
    任务:
    io  密集型的任务: 执行任务的过程中,大量的时间浪费在等待上面
        --> 更适合多线程
        --> 多线程之间的切换开销小,多进程切换的开销大
    cpu 密集型任务: 会有大量的计算,没有任务需要等待
        --> 更适合多进程
        --> 需要更多的计算
    
    在字符串里面匹配指定字符              字符串存在内存里面,需要到内存里面匹配指定内容 cpu
    往列表里面添加100万个数据              cpu
    将列表里面的100万个数据保存到本地      io+cpu
    读取excel文件                      io
    
    只要是与网络相关的任务,都是io密集型任务
    
    录播两小时两分!(大多数人掌握一门语言就足够了)
        
"""