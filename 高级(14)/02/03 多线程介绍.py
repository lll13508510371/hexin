import time
import threading


def download():
    print('开始下载文件')
    time.sleep(3)
    print('完成下载文件')


def upload():
    print('开始上传文件')
    time.sleep(3)
    print('完成上传文件')


# download()
# upload()

# 多线程的作用是将普通对象变成多线程对象
download_thread = threading.Thread(target=download)
download_thread.start()
upload_thread = threading.Thread(target=upload)
upload_thread.start()
'''
两个多线程任务都是同时进行的
'''