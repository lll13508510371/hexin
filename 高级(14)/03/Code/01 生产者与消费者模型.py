import queue
import random
import threading
import time


def producer(pipe):
    """生产者 厨师做包子
       pipe管道 --> 蒸笼
    """
    index = 1
    while True:
        # random.random() 一秒钟以内
        time.sleep(random.random())
        item = f'第{index}个包子'
        print('厨师做出了', item)
        pipe.put(item)  # 默认会是阻塞的
        index += 1


def consumer(pipe):
    """消费者 客户吃包子"""
    while True:
        time.sleep(random.randint(1, 3))
        message = pipe.get()
        print(f'消费者吃了{message}')


if __name__ == '__main__':
    pipeline = queue.Queue(maxsize=10)
    # producer(pipe=pipeline)
    # consumer(pipe=pipeline)
    threading.Thread(target=producer, args=(pipeline,)).start()
    threading.Thread(target=consumer, args=(pipeline,)).start()
