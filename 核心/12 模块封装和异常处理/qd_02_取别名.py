# 需求： 运行后暂停2秒打印hello
# import time  # 时间模块
#
#
# time.sleep(2)
# print('hello')

# 把time模块取了一个别名 --> tt
# import time as tt
#
# tt.sleep(2)
# print('hello')

# 从time中导入sleep功能, 把这个功能取了一个别名
from time import sleep as sl

sl(2)
print('hello')


