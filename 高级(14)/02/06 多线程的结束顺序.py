import time
import threading
import random


def download(start_time):
    print('开始下载文件')
    time.sleep(random.random())
    print('完成下载文件')
    print('子线程 download 结束的时间:\t', time.time() - start_time)


def upload(start_time):
    print('开始上传文件')
    time.sleep(random.random())
    print('完成上传文件')
    print('子线程 upload 结束的时间:\t', time.time() - start_time)


# start_time = time.time()
# download()
# upload()
# print(time.time() - start_time)
start_time = time.time()
# 多线程的作用是将普通对象变成多线程对象
download_thread = threading.Thread(target=download, args=(start_time,))
download_thread.start()
upload_thread = threading.Thread(target=upload, args=(start_time,))
upload_thread.start()
print('主线程的结束时间', time.time() - start_time)


'''
开始下载文件
开始上传文件主线程的结束时间 0.0009694099426269531
(多线程,运行upload的过程当中,#print('主线程的结束时间', time.time() - start_time)执行)
'''