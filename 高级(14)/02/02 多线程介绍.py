import time
import threading


def work():
    """只有函数对象才能使用多线程"""
    print('5. 洗茶杯：1min')
    time.sleep(1)
    print('6. 放茶叶：1min')
    time.sleep(1)
    return None


start_time = time.time()
print('1. 洗茶壶: 1min')
time.sleep(1)
print('2. 灌凉水：1min')
time.sleep(1)
print('3. 烧水：1min')
time.sleep(1)
print('4. 等水烧开：3min')
# 需要先发布任务,在等水烧开
work_thread = threading.Thread(target=work)  # work, work() --> None
work_thread.start()
time.sleep(1)
time.sleep(1)
time.sleep(1)
# print('5. 洗茶杯：1min')
# time.sleep(1)
# print('6. 放茶叶：1min')
# time.sleep(1)
print('7. 泡茶：1min')
time.sleep(1)
print('总运行时间:\t', time.time() - start_time)
