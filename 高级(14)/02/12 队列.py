import queue

# 1. 创建一个队列  需要设置队列最大的容量
q = queue.Queue(maxsize=10)

for i in range(1, 12):
    item = f'数据{i}'
    print(item)
    q.put(item, block=True, timeout=3)
print(f'q:{q}')
print(f'q.size():{q.qsize()}')
for i in range(1, 12):
    print(f'取出第{i}', q.get(block=True))

"""
    block       是否进行阻塞放数据(put)  是否进行等待取数据(get)
    timeout     等待的时间
"""