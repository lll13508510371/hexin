import random
import time
import threading
import requests

# 创建一把锁
lock = threading.Lock()


def download(url, no, name):
    time.sleep(random.random())
    # lock.acquire()
    # 什么是敏感数据 ? 共享的变量就是敏感数据, 全局变量,文件,数据库
    with lock:  # 使用with进行加锁,就不需要释放锁了
        with open('demo.txt', mode='a', encoding='utf-8') as f:
            f.write(f'no:{no} - name:{name} - url:{url}\n')
    # lock.release()  # 如果忘记释放锁,就是死锁
    print(url)


urls = ['https://www.baidu.com?page={}'.format(page) for page in range(1, 101)]
index = 0
for url in urls:
    index += 1
    # print(url)
    # download(url, index, name='百度')
    # 位置参数通过 args 的元祖传递进去
    # 关键字参数通过 kwargs 的字典传送进去
    t1 = threading.Thread(target=download, args=(url, index,), kwargs={"name": "百度"})
    t1.start()
