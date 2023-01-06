import time
import threading
import random


def download(url):
    time.sleep(random.random())
    print('完成下载文件', url)
    with open('data.txt', mode='a', encoding='utf-8') as file:
        file.write(url + '\n')


urls = ['https://www.baidu.com?page={}'.format(page) for page in range(1, 11)]

for url in urls:
    # download(url)
    # 位置参数通过 args 的元祖传递进去
    # 关键字参数通过 kwargs 的字典传送进去
    t1 = threading.Thread(target=download, args=(url,), kwargs={})
    t1.start()


"""
    多线程没有执行顺序 ?  
    如果想要结果有顺序
"""