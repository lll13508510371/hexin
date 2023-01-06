import time
import threading


def download(url):
    print('开始下载文件', url)
    time.sleep(1)
    print('完成下载文件', url)
    return None


urls = ['https://www.baidu.com?page={}'.format(page) for page in range(1, 11)]
# print(urls)
for url in urls:
    # download(url)
    # 位置参数通过 args 的元祖传递进去
    # 关键字参数通过 kwargs 的字典传送进去
    t1 = threading.Thread(target=download, args=(url,), kwargs={})
    t1.start()

