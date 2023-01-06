import time
import threading
import random


def add(num):
    num += 1


import dis

dis.dis(add)

"""
    num = 1
    
    第一个人
        锁定变量        num
        锁定常量        1
        执行加法运算     
                        第二个人
                        锁定变量
                        锁定常量
                        执行加法运算  num = 2
        释放变量
        释放常量
        返回结果进行覆盖
        num = 2
                        释放变量
                        释放常量
                        返回结果进行覆盖
                        num = 2
"""

"""
 7            0 LOAD_FAST                0 (num)        # 锁定变量
              2 LOAD_CONST               1 (1)          # 锁定常量
              4 INPLACE_ADD                             # 执行加法运算
              6 STORE_FAST               0 (num)        # 释放变量
              8 LOAD_CONST               0 (None)       # 释放常量
             10 RETURN_VALUE                            # 返回结果进行覆盖
"""