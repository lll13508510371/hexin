baidu_urls = ['https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/',
              'https://www.baidu.com/', 'https://www.baidu.com/']

""" 
    定义一个请求方法 get_html 用于并返回网页数据
    定义一个保存方法 save_html 用于保存返回的网页数据
    
    多进程请求 baidu_urls ，计算所有请求的时间 (不是所有请求的时间之和 --> 各个请求的时间分别列出来
    --> 所有请求的时间)
    然后去将每一个文件分别标号保存，保存文件名为
    baidu_1.html,baidu_2.html,baidu_3.html,
    baidu_4.html,baidu_5.html,baidu_6.html,
    baidu_7.html,baidu_8.html,baidu_9.html,
    baidu_10.html


如果不会爬虫, 可以参照下面的请求，也可以微信私聊正心
>>> import requests
>>> response = requests.get('https://www.baidu.com/')
>>> html = response.text
"""
import multiprocessing
import requests
import time


# response = requests.get('https://www.baidu.com/')
# html = response.text
# print(html)
def get_html(url):
    response = requests.get(url)
    html = response.text
    return html


def save_html(html, num):
    with open(f'baidu_{num}.html', mode='w', encoding='utf-8') as f:
        f.write(html)


def download(url, num):
    start_time = time.time()
    html = get_html(url)
    request_time = time.time() - start_time
    save_html(html, num)
    # '+'用于字符串连接,不能连接其它类型的数据,其它类型数据要用','连接
    print('请求的时间:\t', request_time)


if __name__ == '__main__':
    # start_time = time.time()

    num = 1

    for url in baidu_urls:
        download_process = multiprocessing.Process(target=download,
                                                   args=(url, num))
        download_process.start()
        num += 1
        # request_time = time.time() - start_time
        # print(request_time)
    # print('运行时间\t', time.time() - start_time)
