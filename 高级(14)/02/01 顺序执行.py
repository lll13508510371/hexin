import time

# time.time() 获取当前的时间戳
start_time = time.time()
print('1. 洗茶壶: 1min')
time.sleep(1)  # 延时1秒模拟等待时间
print('2. 灌凉水：1min')
time.sleep(1)
print('3. 烧水：1min')
time.sleep(1)
print('4. 等水烧开：3min')
time.sleep(1)
time.sleep(1)
time.sleep(1)
print('5. 洗茶杯：1min')
time.sleep(1)
print('6. 放茶叶：1min')
time.sleep(1)
print('7. 泡茶：1min')
time.sleep(1)
print('总运行时间:\t', time.time() - start_time)
