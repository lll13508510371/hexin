import random
import threading


# random.random()  # 1以内

# 多线程结果显示不分先后,主要它们是同时出现的就能说明它们是同时进行的
def append(list_):
    list_.append(1)
    list_.append(2)
    list_.append(3)
    print('list\t', list_)


arr = list()
threading.Thread(target=append, args=(arr,)).start()
print(arr)
threading.Thread(target=append, args=(arr,)).start()
print(arr)
print(arr)

'''
多线程是共享数据的
'''
'''
网易云APP都关闭了(主进程结束)后台音乐还在播放,合理吗?不合理,所以需要进程守护
'''